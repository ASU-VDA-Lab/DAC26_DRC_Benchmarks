import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon95")


m4_layer = layout.layer(40, 0)

m4 = pya.Polygon([pya.Point(0, 0), pya.Point(100, 0), pya.Point(100, 100), pya.Point(0, 100)])
top_cell.shapes(m4_layer).insert(m4)

layout.write("../gds/Polygon95.gds")
