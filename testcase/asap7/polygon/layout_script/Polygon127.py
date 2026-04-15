import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon127")


m6_layer = layout.layer(60, 0)

m6_1 = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 128), pya.Point(0, 128)])
top_cell.shapes(m6_layer).insert(m6_1)

m6_2 = pya.Polygon([pya.Point(0, 240), pya.Point(192, 240), pya.Point(192, 368), pya.Point(0, 368)])
top_cell.shapes(m6_layer).insert(m6_2)

layout.write("../gds/Polygon127.gds")
