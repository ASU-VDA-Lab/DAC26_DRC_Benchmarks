import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon259")


v1_layer = layout.layer(21, 0)
m1_layer = layout.layer(19, 0)
m2_layer = layout.layer(20, 0)

v1_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v1_layer).insert(v1_1)

v1_2 = pya.Polygon([pya.Point(152, 120), pya.Point(224, 120), pya.Point(224, 192), pya.Point(152, 192)])
top_cell.shapes(v1_layer).insert(v1_2)

m2_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(m2_layer).insert(m2_1)

m2_2 = pya.Polygon([pya.Point(152, 120), pya.Point(224, 120), pya.Point(224, 192), pya.Point(152, 192)])
top_cell.shapes(m2_layer).insert(m2_2)

m1 = pya.Polygon([pya.Point(-20, -8), pya.Point(244, -8), pya.Point(244, 212), pya.Point(-20, 212)])
top_cell.shapes(m1_layer).insert(m1)

layout.write("../gds/Polygon259.gds")
