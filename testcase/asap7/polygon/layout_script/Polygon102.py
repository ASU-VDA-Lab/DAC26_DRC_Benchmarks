import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon102")


m4_layer = layout.layer(40, 0)

m4_a = pya.Polygon([pya.Point(0, 0), pya.Point(384, 0), pya.Point(384, 96), pya.Point(0, 96)])
top_cell.shapes(m4_layer).insert(m4_a)

m4_b = pya.Polygon([pya.Point(480, 192), pya.Point(1152, 192), pya.Point(1152, 288), pya.Point(480, 288)])
top_cell.shapes(m4_layer).insert(m4_b)

m4_c = pya.Polygon([pya.Point(0, 384), pya.Point(1152, 384), pya.Point(1152, 480), pya.Point(0, 480)])
top_cell.shapes(m4_layer).insert(m4_c)

m4_d = pya.Polygon([pya.Point(0, 768), pya.Point(192, 768), pya.Point(192, 1168), pya.Point(0, 1168)])
top_cell.shapes(m4_layer).insert(m4_d)

m4_e = pya.Polygon([pya.Point(96, 1264), pya.Point(288, 1264), pya.Point(288, 1664), pya.Point(96, 1664)])
top_cell.shapes(m4_layer).insert(m4_e)

layout.write("../gds/Polygon102.gds")
