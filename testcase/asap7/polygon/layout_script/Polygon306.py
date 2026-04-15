import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon306")


m7_layer = layout.layer(70, 0)
m8_layer = layout.layer(80, 0)
v7_layer = layout.layer(75, 0)

m8 = pya.Polygon([pya.Point(0, -44), pya.Point(256, -44), pya.Point(256, 400), pya.Point(0, 400)])
top_cell.shapes(m8_layer).insert(m8)

v7 = pya.Polygon([pya.Point(64, 0), pya.Point(192, 0), pya.Point(192, 128), pya.Point(64, 128)])
top_cell.shapes(v7_layer).insert(v7)

m7 = pya.Polygon([pya.Point(20, -44), pya.Point(236, -44), pya.Point(236, 172), pya.Point(20, 172)])
top_cell.shapes(m7_layer).insert(m7)

layout.write("../gds/Polygon306.gds")
