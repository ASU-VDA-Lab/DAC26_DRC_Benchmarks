import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon71")


m1_layer = layout.layer(19, 0)

m1_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 120), pya.Point(0, 120)])
top_cell.shapes(m1_layer).insert(m1_1)

m1_2 = pya.Polygon([pya.Point(152, 0), pya.Point(224, 0), pya.Point(224, 200), pya.Point(152, 200)])
top_cell.shapes(m1_layer).insert(m1_2)

layout.write("../gds/Polygon71.gds")
