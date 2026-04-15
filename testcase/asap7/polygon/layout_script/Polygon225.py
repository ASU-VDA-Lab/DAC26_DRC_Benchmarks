import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon225")


active_layer = layout.layer(11, 0)
pselect_layer = layout.layer(13, 0)
sramdrc_layer = layout.layer(99, 0)

active = pya.Polygon([pya.Point(40, 60), pya.Point(200, 60), pya.Point(200, 168), pya.Point(40, 168)])
top_cell.shapes(active_layer).insert(active)

sramdrc = pya.Polygon([pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 240), pya.Point(0, 240)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

pselect = pya.Polygon([pya.Point(0, 0), pya.Point(240, 0), pya.Point(240, 240), pya.Point(0, 240)])
top_cell.shapes(pselect_layer).insert(pselect)

layout.write("../gds/Polygon225.gds")
