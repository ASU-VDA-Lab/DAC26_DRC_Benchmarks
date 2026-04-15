import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon116")


m5_layer = layout.layer(50, 0)

m5_a = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 400), pya.Point(0, 400)])
top_cell.shapes(m5_layer).insert(m5_a)

m5_b = pya.Polygon([pya.Point(192, 96), pya.Point(288, 96), pya.Point(288, 496), pya.Point(192, 496)])
top_cell.shapes(m5_layer).insert(m5_b)

layout.write("../gds/Polygon116.gds")
