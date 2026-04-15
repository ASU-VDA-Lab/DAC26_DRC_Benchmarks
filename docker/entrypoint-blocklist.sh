#BSD 3-Clause License
#
#Copyright (c) 2026, ASU-VDA-Lab
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#3. Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#!/bin/bash
# Resolve each domain in blocklist.txt to its current IP(s) and add REJECT
# OUTPUT rules in iptables.  Then exec whatever command was passed to the
# container.
#
# Requires:
#   docker run ... --cap-add=NET_ADMIN ...
#
# Blocklist is read from either:
#   - /etc/klayout-blocklist  (baked into the image — see below)
#   - $BLOCKLIST_FILE env var  (override)

set -e

BLOCKLIST_FILE="${BLOCKLIST_FILE:-/etc/klayout-blocklist}"

# If no blocklist is mounted / baked in, fall back to a conservative default.
if [ ! -f "$BLOCKLIST_FILE" ]; then
    BLOCKLIST_FILE=$(mktemp)
    cat > "$BLOCKLIST_FILE" <<'EOF'
# --- klayout official ---
klayout.org
www.klayout.org
# --- Python package index ---
pypi.org
files.pythonhosted.org
pythonhosted.org
python.org
www.python.org
# --- GitHub (source code) ---
github.com
api.github.com
raw.githubusercontent.com
codeload.github.com
objects.githubusercontent.com
gist.github.com
# --- Other source hosts ---
gitlab.com
bitbucket.org
# --- Conda / Anaconda ---
conda.anaconda.org
repo.anaconda.com
pkgs.anaconda.com
# --- Other package distribution ---
sourceforge.net
dl.fedoraproject.org
rpmfind.net
mirrors.kernel.org
mirrorservice.org
ftp.gnu.org
EOF
fi

blocked_count=0
failed_count=0

echo "[entrypoint] Programming klayout-related domain blocklist..."

# First drop any existing OUTPUT rules that might interfere (idempotent).
# We do NOT flush the table entirely because docker installs default rules.

while IFS= read -r line; do
    # Strip comments and whitespace.
    domain=$(echo "$line" | sed 's/#.*//' | xargs)
    [ -z "$domain" ] && continue

    ips=$(getent ahosts "$domain" 2>/dev/null | awk '{print $1}' | sort -u)
    if [ -z "$ips" ]; then
        echo "  [skip]  $domain (DNS resolution failed)"
        failed_count=$((failed_count + 1))
        continue
    fi

    for ip in $ips; do
        # REJECT gives a fast error to the client (vs DROP which silently
        # times out).  Skips duplicate rules automatically via -C check.
        if iptables -C OUTPUT -d "$ip" -j REJECT --reject-with icmp-host-prohibited 2>/dev/null; then
            : # rule already present
        else
            if iptables -A OUTPUT -d "$ip" -j REJECT --reject-with icmp-host-prohibited 2>/dev/null; then
                blocked_count=$((blocked_count + 1))
            fi
        fi
    done
    echo "  [block] $domain -> $ips"
done < "$BLOCKLIST_FILE"

echo "[entrypoint] Blocklist active: $blocked_count IP rules installed ($failed_count domains unresolved)."

# --- Exec the real command --------------------------------------------------
if [ $# -eq 0 ]; then
    exec bash
else
    exec "$@"
fi
