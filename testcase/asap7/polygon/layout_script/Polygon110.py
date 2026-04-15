import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon110")


m5_layer = layout.layer(50, 0)

m5_1 = pya.Polygon([pya.Point(96, 96), pya.Point(192, 96), pya.Point(192, 288), pya.Point(96, 288)])
top_cell.shapes(m5_layer).insert(m5_1)

m5_2 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 192), pya.Point(0, 192)])
top_cell.shapes(m5_layer).insert(m5_2)

layout.write("../gds/Polygon110.gds")
