import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon159")


m8_layer = layout.layer(80, 0)

m8_1 = pya.Polygon([pya.Point(0, 0), pya.Point(2000, 0), pya.Point(2000, 2000), pya.Point(0, 2000)])
top_cell.shapes(m8_layer).insert(m8_1)

m8_2 = pya.Polygon([pya.Point(2400, 0), pya.Point(2560, 0), pya.Point(2560, 752), pya.Point(2400, 752)])
top_cell.shapes(m8_layer).insert(m8_2)

layout.write("../gds/Polygon159.gds")
