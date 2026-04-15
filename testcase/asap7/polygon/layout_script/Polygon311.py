import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon311")


m7_layer = layout.layer(70, 0)
m8_layer = layout.layer(80, 0)
v7_layer = layout.layer(75, 0)

v7 = pya.Polygon([pya.Point(0, 0), pya.Point(112, 0), pya.Point(112, 112), pya.Point(0, 112)])
top_cell.shapes(v7_layer).insert(v7)

m7 = pya.Polygon([pya.Point(-60, -60), pya.Point(268, -60), pya.Point(268, 172), pya.Point(-60, 172)])
top_cell.shapes(m7_layer).insert(m7)

m8 = pya.Polygon([pya.Point(-60, -60), pya.Point(172, -60), pya.Point(172, 268), pya.Point(-60, 268)])
top_cell.shapes(m8_layer).insert(m8)

layout.write("../gds/Polygon311.gds")
