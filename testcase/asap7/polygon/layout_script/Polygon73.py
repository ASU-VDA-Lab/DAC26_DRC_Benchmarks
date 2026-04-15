import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon73")


m1_layer = layout.layer(19, 0)

m1_1 = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 200), pya.Point(0, 200)])
top_cell.shapes(m1_layer).insert(m1_1)

m1_2 = pya.Polygon([pya.Point(0, 312), pya.Point(80, 312), pya.Point(80, 512), pya.Point(0, 512)])
top_cell.shapes(m1_layer).insert(m1_2)

layout.write("../gds/Polygon73.gds")
