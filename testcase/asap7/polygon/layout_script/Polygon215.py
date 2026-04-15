import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon215")


active_layer = layout.layer(11, 0)
nwell_layer = layout.layer(1, 0)
nselect_layer = layout.layer(12, 0)
sramdrc_layer = layout.layer(99, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(160, 0), pya.Point(160, 216), pya.Point(0, 216)])
top_cell.shapes(active_layer).insert(active)

sramdrc = pya.Polygon([pya.Point(-40, -40), pya.Point(200, -40), pya.Point(200, 256), pya.Point(-40, 256)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

nwell = pya.Polygon([pya.Point(200, 0), pya.Point(1200, 0), pya.Point(1200, 800), pya.Point(200, 800)])
top_cell.shapes(nwell_layer).insert(nwell)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(360, -120), pya.Point(360, 336), pya.Point(-200, 336)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon215.gds")
