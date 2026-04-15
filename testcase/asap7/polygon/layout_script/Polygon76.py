import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon76")


m1_layer = layout.layer(19, 0)

m1 = pya.Polygon([pya.Point(0, 0), pya.Point(64, 0), pya.Point(64, 200), pya.Point(0, 200)])
top_cell.shapes(m1_layer).insert(m1)

layout.write("../gds/Polygon76.gds")
