import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon254")


v1_layer = layout.layer(21, 0)
m1_layer = layout.layer(19, 0)
m2_layer = layout.layer(20, 0)

v1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v1_layer).insert(v1)

m1 = pya.Polygon([pya.Point(-4, -4), pya.Point(76, -4), pya.Point(76, 76), pya.Point(-4, 76)])
top_cell.shapes(m1_layer).insert(m1)

m2 = pya.Polygon([pya.Point(0, -24), pya.Point(72, -24), pya.Point(72, 96), pya.Point(0, 96)])
top_cell.shapes(m2_layer).insert(m2)

layout.write("../gds/Polygon254.gds")
