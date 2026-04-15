import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon310")


m7_layer = layout.layer(70, 0)
m8_layer = layout.layer(80, 0)
v7_layer = layout.layer(75, 0)

v7_1 = pya.Polygon([pya.Point(0, 0), pya.Point(128, 0), pya.Point(128, 128), pya.Point(0, 128)])
top_cell.shapes(v7_layer).insert(v7_1)

v7_2 = pya.Polygon([pya.Point(216, 216), pya.Point(344, 216), pya.Point(344, 344), pya.Point(216, 344)])
top_cell.shapes(v7_layer).insert(v7_2)

m7 = pya.Polygon([pya.Point(-60, -60), pya.Point(404, -60), pya.Point(404, 404), pya.Point(-60, 404)])
top_cell.shapes(m7_layer).insert(m7)

m8 = pya.Polygon([pya.Point(-60, -60), pya.Point(404, -60), pya.Point(404, 404), pya.Point(-60, 404)])
top_cell.shapes(m8_layer).insert(m8)

layout.write("../gds/Polygon310.gds")
