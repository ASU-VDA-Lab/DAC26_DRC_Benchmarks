import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon96")


m4_layer = layout.layer(40, 0)

m4_1 = pya.Polygon([pya.Point(96, 96), pya.Point(288, 96), pya.Point(288, 192), pya.Point(96, 192)])
top_cell.shapes(m4_layer).insert(m4_1)

m4_2 = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 96), pya.Point(0, 96)])
top_cell.shapes(m4_layer).insert(m4_2)

layout.write("../gds/Polygon96.gds")
