import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon284")


m4_layer = layout.layer(40, 0)
m5_layer = layout.layer(50, 0)
v4_layer = layout.layer(45, 0)

v4_1 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 96), pya.Point(0, 96)])
top_cell.shapes(v4_layer).insert(v4_1)

v4_2 = pya.Polygon([pya.Point(208, 0), pya.Point(304, 0), pya.Point(304, 96), pya.Point(208, 96)])
top_cell.shapes(v4_layer).insert(v4_2)

m4 = pya.Polygon([pya.Point(-60, -60), pya.Point(364, -60), pya.Point(364, 300), pya.Point(-60, 300)])
top_cell.shapes(m4_layer).insert(m4)

m5 = pya.Polygon([pya.Point(-60, -60), pya.Point(364, -60), pya.Point(364, 300), pya.Point(-60, 300)])
top_cell.shapes(m5_layer).insert(m5)

layout.write("../gds/Polygon284.gds")
