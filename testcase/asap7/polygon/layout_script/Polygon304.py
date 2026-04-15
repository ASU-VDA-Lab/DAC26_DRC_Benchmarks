import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon304")


m7_layer = layout.layer(70, 0)
m8_layer = layout.layer(80, 0)
v7_layer = layout.layer(75, 0)

v7 = pya.Polygon([pya.Point(0, 0), pya.Point(128, 0), pya.Point(128, 128), pya.Point(0, 128)])
top_cell.shapes(v7_layer).insert(v7)

m7 = pya.Polygon([pya.Point(-44, -44), pya.Point(172, -44), pya.Point(172, 172), pya.Point(-44, 172)])
top_cell.shapes(m7_layer).insert(m7)

m8 = pya.Polygon([pya.Point(-44, -44), pya.Point(172, -44), pya.Point(172, 104), pya.Point(-44, 104)])
top_cell.shapes(m8_layer).insert(m8)

layout.write("../gds/Polygon304.gds")
