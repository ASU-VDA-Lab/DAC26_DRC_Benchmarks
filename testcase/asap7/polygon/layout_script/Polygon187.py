import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon187")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)

nselect = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 200), pya.Point(0, 200)])
top_cell.shapes(nselect_layer).insert(nselect)

active = pya.Polygon([pya.Point(320, 44), pya.Point(480, 44), pya.Point(480, 152), pya.Point(320, 152)])
top_cell.shapes(active_layer).insert(active)

layout.write("../gds/Polygon187.gds")
