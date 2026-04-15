import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon155")


m8_layer = layout.layer(80, 0)

m8_1 = pya.Polygon([pya.Point(0, 0), pya.Point(384, 0), pya.Point(384, 316), pya.Point(0, 316)])
top_cell.shapes(m8_layer).insert(m8_1)

m8_2 = pya.Polygon([pya.Point(560, 0), pya.Point(944, 0), pya.Point(944, 316), pya.Point(560, 316)])
top_cell.shapes(m8_layer).insert(m8_2)

layout.write("../gds/Polygon155.gds")
