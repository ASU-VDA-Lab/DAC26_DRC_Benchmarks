import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon286")


m4_layer = layout.layer(40, 0)
m5_layer = layout.layer(50, 0)
v4_layer = layout.layer(45, 0)

v4_1 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 96), pya.Point(0, 96)])
top_cell.shapes(v4_layer).insert(v4_1)

v4_2 = pya.Polygon([pya.Point(160, 160), pya.Point(256, 160), pya.Point(256, 256), pya.Point(160, 256)])
top_cell.shapes(v4_layer).insert(v4_2)

m4 = pya.Polygon([pya.Point(-60, -60), pya.Point(316, -60), pya.Point(316, 316), pya.Point(-60, 316)])
top_cell.shapes(m4_layer).insert(m4)

m5 = pya.Polygon([pya.Point(-60, -60), pya.Point(316, -60), pya.Point(316, 316), pya.Point(-60, 316)])
top_cell.shapes(m5_layer).insert(m5)

layout.write("../gds/Polygon286.gds")
