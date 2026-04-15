import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon70")


m1_layer = layout.layer(19, 0)

m1_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 200), pya.Point(0, 200)])
top_cell.shapes(m1_layer).insert(m1_1)

m1_2 = pya.Polygon([pya.Point(128, 0), pya.Point(200, 0), pya.Point(200, 200), pya.Point(128, 200)])
top_cell.shapes(m1_layer).insert(m1_2)

layout.write("../gds/Polygon70.gds")
