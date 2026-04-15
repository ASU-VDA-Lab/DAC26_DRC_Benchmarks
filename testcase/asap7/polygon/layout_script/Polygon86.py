import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon86")


m2_layer = layout.layer(20, 0)

m2 = pya.Polygon([pya.Point(0, 0), pya.Point(64, 0), pya.Point(64, 200), pya.Point(0, 200)])
top_cell.shapes(m2_layer).insert(m2)

layout.write("../gds/Polygon86.gds")
