import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon292")


m5_layer = layout.layer(50, 0)
m6_layer = layout.layer(60, 0)
v5_layer = layout.layer(55, 0)

v5_1 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 96), pya.Point(0, 96)])
top_cell.shapes(v5_layer).insert(v5_1)

v5_2 = pya.Polygon([pya.Point(208, 0), pya.Point(304, 0), pya.Point(304, 96), pya.Point(208, 96)])
top_cell.shapes(v5_layer).insert(v5_2)

m5 = pya.Polygon([pya.Point(-60, -60), pya.Point(364, -60), pya.Point(364, 300), pya.Point(-60, 300)])
top_cell.shapes(m5_layer).insert(m5)

m6 = pya.Polygon([pya.Point(-60, -60), pya.Point(364, -60), pya.Point(364, 300), pya.Point(-60, 300)])
top_cell.shapes(m6_layer).insert(m6)

layout.write("../gds/Polygon292.gds")
