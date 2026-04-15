import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon300")


m6_layer = layout.layer(60, 0)
m7_layer = layout.layer(70, 0)
v6_layer = layout.layer(65, 0)

v6_1 = pya.Polygon([pya.Point(0, 0), pya.Point(128, 0), pya.Point(128, 128), pya.Point(0, 128)])
top_cell.shapes(v6_layer).insert(v6_1)

v6_2 = pya.Polygon([pya.Point(288, 0), pya.Point(416, 0), pya.Point(416, 128), pya.Point(288, 128)])
top_cell.shapes(v6_layer).insert(v6_2)

m6 = pya.Polygon([pya.Point(-60, -60), pya.Point(476, -60), pya.Point(476, 300), pya.Point(-60, 300)])
top_cell.shapes(m6_layer).insert(m6)

m7 = pya.Polygon([pya.Point(-60, -60), pya.Point(476, -60), pya.Point(476, 300), pya.Point(-60, 300)])
top_cell.shapes(m7_layer).insert(m7)

layout.write("../gds/Polygon300.gds")
