import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon153")


m8_layer = layout.layer(80, 0)

m8_1 = pya.Polygon([pya.Point(0, 0), pya.Point(360, 0), pya.Point(360, 360), pya.Point(0, 360)])
top_cell.shapes(m8_layer).insert(m8_1)

m8_2 = pya.Polygon([pya.Point(480, 0), pya.Point(840, 0), pya.Point(840, 360), pya.Point(480, 360)])
top_cell.shapes(m8_layer).insert(m8_2)

layout.write("../gds/Polygon153.gds")
