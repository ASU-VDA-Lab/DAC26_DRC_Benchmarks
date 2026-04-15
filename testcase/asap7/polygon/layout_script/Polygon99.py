import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon99")


m4_layer = layout.layer(40, 0)

m4_1 = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 96), pya.Point(0, 96)])
top_cell.shapes(m4_layer).insert(m4_1)

m4_2 = pya.Polygon([pya.Point(0, 176), pya.Point(192, 176), pya.Point(192, 272), pya.Point(0, 272)])
top_cell.shapes(m4_layer).insert(m4_2)

layout.write("../gds/Polygon99.gds")
