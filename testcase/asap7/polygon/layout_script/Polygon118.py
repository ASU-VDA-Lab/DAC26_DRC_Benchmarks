import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon118")


m5_layer = layout.layer(50, 0)

m5 = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 192), pya.Point(0, 192)])
top_cell.shapes(m5_layer).insert(m5)

layout.write("../gds/Polygon118.gds")
