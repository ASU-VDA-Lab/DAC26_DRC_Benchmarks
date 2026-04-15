import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon290")


m5_layer = layout.layer(50, 0)
m6_layer = layout.layer(60, 0)
v5_layer = layout.layer(55, 0)

m6 = pya.Polygon([pya.Point(0, -44), pya.Point(192, -44), pya.Point(192, 400), pya.Point(0, 400)])
top_cell.shapes(m6_layer).insert(m6)

v5 = pya.Polygon([pya.Point(48, 0), pya.Point(144, 0), pya.Point(144, 96), pya.Point(48, 96)])
top_cell.shapes(v5_layer).insert(v5)

m5 = pya.Polygon([pya.Point(4, -44), pya.Point(188, -44), pya.Point(188, 140), pya.Point(4, 140)])
top_cell.shapes(m5_layer).insert(m5)

layout.write("../gds/Polygon290.gds")
