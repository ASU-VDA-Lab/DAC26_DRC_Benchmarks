import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon12")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(40, 0), pya.Point(40, 216), pya.Point(0, 216)])
top_cell.shapes(active_layer).insert(active)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(240, -120), pya.Point(240, 336), pya.Point(-200, 336)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon12.gds")
