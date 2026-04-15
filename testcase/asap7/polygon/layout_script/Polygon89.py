import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon89")


m3_layer = layout.layer(30, 0)

m3_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 120), pya.Point(0, 120)])
top_cell.shapes(m3_layer).insert(m3_1)

m3_2 = pya.Polygon([pya.Point(152, 0), pya.Point(224, 0), pya.Point(224, 200), pya.Point(152, 200)])
top_cell.shapes(m3_layer).insert(m3_2)

layout.write("../gds/Polygon89.gds")
