import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon287")


m4_layer = layout.layer(40, 0)
m5_layer = layout.layer(50, 0)
v4_layer = layout.layer(45, 0)

v4 = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 80), pya.Point(0, 80)])
top_cell.shapes(v4_layer).insert(v4)

m4 = pya.Polygon([pya.Point(-60, -60), pya.Point(140, -60), pya.Point(140, 236), pya.Point(-60, 236)])
top_cell.shapes(m4_layer).insert(m4)

m5 = pya.Polygon([pya.Point(-60, -60), pya.Point(236, -60), pya.Point(236, 140), pya.Point(-60, 140)])
top_cell.shapes(m5_layer).insert(m5)

layout.write("../gds/Polygon287.gds")
