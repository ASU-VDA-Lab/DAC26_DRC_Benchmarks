import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon160")


m8_layer = layout.layer(80, 0)

m8_1 = pya.Polygon([pya.Point(0, 0), pya.Point(4800, 0), pya.Point(4800, 4800), pya.Point(0, 4800)])
top_cell.shapes(m8_layer).insert(m8_1)

m8_2 = pya.Polygon([pya.Point(8000, 0), pya.Point(12800, 0), pya.Point(12800, 4800), pya.Point(8000, 4800)])
top_cell.shapes(m8_layer).insert(m8_2)

layout.write("../gds/Polygon160.gds")
