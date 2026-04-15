import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon1")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(108, 0), pya.Point(108, 108), pya.Point(0, 108)])
top_cell.shapes(active_layer).insert(active)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(308, -120), pya.Point(308, 228), pya.Point(-200, 228)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon1.gds")
