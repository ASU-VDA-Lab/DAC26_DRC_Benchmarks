import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon307")


v7_layer = layout.layer(75, 0)
m7_layer = layout.layer(70, 0)
m8_layer = layout.layer(80, 0)

v7 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 96), pya.Point(0, 96)])
top_cell.shapes(v7_layer).insert(v7)

m7 = pya.Polygon([pya.Point(-44, -44), pya.Point(800, -44), pya.Point(800, 800), pya.Point(-44, 800)])
top_cell.shapes(m7_layer).insert(m7)

m8 = pya.Polygon([pya.Point(-20, -20), pya.Point(800, -20), pya.Point(800, 800), pya.Point(-20, 800)])
top_cell.shapes(m8_layer).insert(m8)

layout.write("../gds/Polygon307.gds")
