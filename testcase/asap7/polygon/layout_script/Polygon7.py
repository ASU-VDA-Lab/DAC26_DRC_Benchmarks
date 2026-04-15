import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon7")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)

active1 = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 108), pya.Point(0, 108)])
top_cell.shapes(active_layer).insert(active1)

active2 = pya.Polygon([pya.Point(0, 188), pya.Point(800, 188), pya.Point(800, 296), pya.Point(0, 296)])
top_cell.shapes(active_layer).insert(active2)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(1000, -120), pya.Point(1000, 416), pya.Point(-200, 416)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon7.gds")
