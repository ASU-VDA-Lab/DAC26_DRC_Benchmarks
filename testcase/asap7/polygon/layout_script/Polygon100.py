import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon100")


m4_layer = layout.layer(40, 0)

m4_1 = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 192), pya.Point(0, 192)])
top_cell.shapes(m4_layer).insert(m4_1)

m4_2 = pya.Polygon([pya.Point(320, 0), pya.Point(512, 0), pya.Point(512, 192), pya.Point(320, 192)])
top_cell.shapes(m4_layer).insert(m4_2)

layout.write("../gds/Polygon100.gds")
