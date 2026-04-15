import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon295")


m5_layer = layout.layer(50, 0)
m6_layer = layout.layer(60, 0)
v5_layer = layout.layer(55, 0)

v5 = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 80), pya.Point(0, 80)])
top_cell.shapes(v5_layer).insert(v5)

m5 = pya.Polygon([pya.Point(-60, -60), pya.Point(236, -60), pya.Point(236, 140), pya.Point(-60, 140)])
top_cell.shapes(m5_layer).insert(m5)

m6 = pya.Polygon([pya.Point(-60, -60), pya.Point(140, -60), pya.Point(140, 236), pya.Point(-60, 236)])
top_cell.shapes(m6_layer).insert(m6)

layout.write("../gds/Polygon295.gds")
