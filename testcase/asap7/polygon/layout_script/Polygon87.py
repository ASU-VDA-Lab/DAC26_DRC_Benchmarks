import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon87")


m3_layer = layout.layer(30, 0)

m3 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 108), pya.Point(0, 108)])
top_cell.shapes(m3_layer).insert(m3)

layout.write("../gds/Polygon87.gds")
