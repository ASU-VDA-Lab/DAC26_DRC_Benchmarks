import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon213")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
sramdrc_layer = layout.layer(99, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(160, 0), pya.Point(160, 216), pya.Point(0, 216)])
top_cell.shapes(active_layer).insert(active)

sramdrc = pya.Polygon([pya.Point(160, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(160, 800)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(360, -120), pya.Point(360, 336), pya.Point(-200, 336)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon213.gds")
