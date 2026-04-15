import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon302")


m6_layer = layout.layer(60, 0)
m7_layer = layout.layer(70, 0)
v6_layer = layout.layer(65, 0)

v6_1 = pya.Polygon([pya.Point(0, 0), pya.Point(128, 0), pya.Point(128, 128), pya.Point(0, 128)])
top_cell.shapes(v6_layer).insert(v6_1)

v6_2 = pya.Polygon([pya.Point(216, 216), pya.Point(344, 216), pya.Point(344, 344), pya.Point(216, 344)])
top_cell.shapes(v6_layer).insert(v6_2)

m6 = pya.Polygon([pya.Point(-60, -60), pya.Point(404, -60), pya.Point(404, 404), pya.Point(-60, 404)])
top_cell.shapes(m6_layer).insert(m6)

m7 = pya.Polygon([pya.Point(-60, -60), pya.Point(404, -60), pya.Point(404, 404), pya.Point(-60, 404)])
top_cell.shapes(m7_layer).insert(m7)

layout.write("../gds/Polygon302.gds")
