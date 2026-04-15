import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon152")


m8_layer = layout.layer(80, 0)


m8 = pya.Polygon([ pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 360), pya.Point(280, 360), pya.Point(280, 400), pya.Point(0, 400), ])
top_cell.shapes(m8_layer).insert(m8)

layout.write("../gds/Polygon152.gds")
