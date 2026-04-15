import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon122")


m5_layer = layout.layer(50, 0)

m5 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 160), pya.Point(0, 160)])
top_cell.shapes(m5_layer).insert(m5)

layout.write("../gds/Polygon122.gds")
