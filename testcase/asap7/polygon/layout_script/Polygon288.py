import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon288")


m5_layer = layout.layer(50, 0)
m6_layer = layout.layer(60, 0)
v5_layer = layout.layer(55, 0)

v5 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 96), pya.Point(0, 96)])
top_cell.shapes(v5_layer).insert(v5)

m5 = pya.Polygon([pya.Point(-44, -44), pya.Point(140, -44), pya.Point(140, 140), pya.Point(-44, 140)])
top_cell.shapes(m5_layer).insert(m5)

m6 = pya.Polygon([pya.Point(-44, -44), pya.Point(140, -44), pya.Point(140, 72), pya.Point(-44, 72)])
top_cell.shapes(m6_layer).insert(m6)

layout.write("../gds/Polygon288.gds")
