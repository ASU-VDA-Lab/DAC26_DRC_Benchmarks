import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon109")


m5_layer = layout.layer(50, 0)

m5 = pya.Polygon([pya.Point(0, 0), pya.Point(100, 0), pya.Point(100, 100), pya.Point(0, 100)])
top_cell.shapes(m5_layer).insert(m5)

layout.write("../gds/Polygon109.gds")
