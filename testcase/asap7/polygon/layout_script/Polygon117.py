import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon117")


m5_layer = layout.layer(50, 0)

m5_1 = pya.Polygon([pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 192), pya.Point(0, 192)])
top_cell.shapes(m5_layer).insert(m5_1)

m5_2 = pya.Polygon([pya.Point(496, 96), pya.Point(896, 96), pya.Point(896, 288), pya.Point(496, 288)])
top_cell.shapes(m5_layer).insert(m5_2)

layout.write("../gds/Polygon117.gds")
