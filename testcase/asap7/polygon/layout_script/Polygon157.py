import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon157")


m8_layer = layout.layer(80, 0)

m8_1 = pya.Polygon([pya.Point(0, 0), pya.Point(360, 0), pya.Point(360, 360), pya.Point(0, 360)])
top_cell.shapes(m8_layer).insert(m8_1)

m8_2 = pya.Polygon([pya.Point(660, 0), pya.Point(1020, 0), pya.Point(1020, 360), pya.Point(660, 360)])
top_cell.shapes(m8_layer).insert(m8_2)

layout.write("../gds/Polygon157.gds")
