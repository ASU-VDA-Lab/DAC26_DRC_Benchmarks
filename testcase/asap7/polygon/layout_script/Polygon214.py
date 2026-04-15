import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon214")


active_layer = layout.layer(11, 0)
nwell_layer = layout.layer(1, 0)
pselect_layer = layout.layer(13, 0)
sramdrc_layer = layout.layer(99, 0)

nwell = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(0, 800)])
top_cell.shapes(nwell_layer).insert(nwell)

sramdrc = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(0, 800)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

active = pya.Polygon([pya.Point(20, 20), pya.Point(240, 20), pya.Point(240, 256), pya.Point(20, 256)])
top_cell.shapes(active_layer).insert(active)

pselect = pya.Polygon([pya.Point(-160, -80), pya.Point(440, -80), pya.Point(440, 376), pya.Point(-160, 376)])
top_cell.shapes(pselect_layer).insert(pselect)

layout.write("../gds/Polygon214.gds")
