import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon11")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 160), pya.Point(0, 160)])
top_cell.shapes(active_layer).insert(active)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(1000, -120), pya.Point(1000, 280), pya.Point(-200, 280)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon11.gds")
