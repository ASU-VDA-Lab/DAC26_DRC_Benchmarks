import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon298")


m6_layer = layout.layer(60, 0)
m7_layer = layout.layer(70, 0)
v6_layer = layout.layer(65, 0)

m7 = pya.Polygon([pya.Point(-44, 0), pya.Point(400, 0), pya.Point(400, 256), pya.Point(-44, 256)])
top_cell.shapes(m7_layer).insert(m7)

v6 = pya.Polygon([pya.Point(0, 64), pya.Point(128, 64), pya.Point(128, 192), pya.Point(0, 192)])
top_cell.shapes(v6_layer).insert(v6)

m6 = pya.Polygon([pya.Point(-44, 20), pya.Point(172, 20), pya.Point(172, 236), pya.Point(-44, 236)])
top_cell.shapes(m6_layer).insert(m6)

layout.write("../gds/Polygon298.gds")
