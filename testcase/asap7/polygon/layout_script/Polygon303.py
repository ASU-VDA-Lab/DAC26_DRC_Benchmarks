import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon303")


m6_layer = layout.layer(60, 0)
m7_layer = layout.layer(70, 0)
v6_layer = layout.layer(65, 0)

v6 = pya.Polygon([pya.Point(0, 0), pya.Point(112, 0), pya.Point(112, 112), pya.Point(0, 112)])
top_cell.shapes(v6_layer).insert(v6)

m6 = pya.Polygon([pya.Point(-60, -60), pya.Point(172, -60), pya.Point(172, 268), pya.Point(-60, 268)])
top_cell.shapes(m6_layer).insert(m6)

m7 = pya.Polygon([pya.Point(-60, -60), pya.Point(268, -60), pya.Point(268, 172), pya.Point(-60, 172)])
top_cell.shapes(m7_layer).insert(m7)

layout.write("../gds/Polygon303.gds")
