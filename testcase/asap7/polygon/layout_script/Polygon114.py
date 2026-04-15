import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon114")


m5_layer = layout.layer(50, 0)

m5_1 = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 192), pya.Point(0, 192)])
top_cell.shapes(m5_layer).insert(m5_1)

m5_2 = pya.Polygon([pya.Point(0, 320), pya.Point(192, 320), pya.Point(192, 512), pya.Point(0, 512)])
top_cell.shapes(m5_layer).insert(m5_2)

layout.write("../gds/Polygon114.gds")
