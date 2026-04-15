import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon164")


m8_layer = layout.layer(80, 0)

m8 = pya.Polygon([ pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 7200), pya.Point(400, 7200), pya.Point(400, 13200), pya.Point(0, 13200), ])
top_cell.shapes(m8_layer).insert(m8)

layout.write("../gds/Polygon164.gds")
