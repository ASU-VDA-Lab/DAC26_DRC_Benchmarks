import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon281")


v4_layer = layout.layer(45, 0)
m4_layer = layout.layer(40, 0)
m5_layer = layout.layer(50, 0)

v4 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 96), pya.Point(0, 96)])
top_cell.shapes(v4_layer).insert(v4)

m4 = pya.Polygon([pya.Point(-20, -20), pya.Point(800, -20), pya.Point(800, 800), pya.Point(-20, 800)])
top_cell.shapes(m4_layer).insert(m4)

m5 = pya.Polygon([pya.Point(-44, -44), pya.Point(800, -44), pya.Point(800, 800), pya.Point(-44, 800)])
top_cell.shapes(m5_layer).insert(m5)

layout.write("../gds/Polygon281.gds")
