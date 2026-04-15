import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon158")


m8_layer = layout.layer(80, 0)

m8_1 = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(0, 800)])
top_cell.shapes(m8_layer).insert(m8_1)

m8_2 = pya.Polygon([pya.Point(1200, 0), pya.Point(2000, 0), pya.Point(2000, 800), pya.Point(1200, 800)])
top_cell.shapes(m8_layer).insert(m8_2)

layout.write("../gds/Polygon158.gds")
