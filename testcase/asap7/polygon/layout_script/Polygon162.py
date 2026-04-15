import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon162")


m8_layer = layout.layer(80, 0)

m8 = pya.Polygon([ pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 2000), pya.Point(220, 2000), pya.Point(220, 3200), pya.Point(0, 3200), ])
top_cell.shapes(m8_layer).insert(m8)

layout.write("../gds/Polygon162.gds")
