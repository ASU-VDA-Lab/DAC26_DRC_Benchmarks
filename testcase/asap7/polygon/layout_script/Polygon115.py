import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon115")


m5_layer = layout.layer(50, 0)

m5_1 = pya.Polygon([pya.Point(0, 0), pya.Point(288, 0), pya.Point(288, 192), pya.Point(0, 192)])
top_cell.shapes(m5_layer).insert(m5_1)

m5_2 = pya.Polygon([pya.Point(320, 320), pya.Point(608, 320), pya.Point(608, 512), pya.Point(320, 512)])
top_cell.shapes(m5_layer).insert(m5_2)

layout.write("../gds/Polygon115.gds")
