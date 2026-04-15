import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon277")


v3_layer = layout.layer(35, 0)
m3_layer = layout.layer(30, 0)
m4_layer = layout.layer(40, 0)

v3_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v3_layer).insert(v3_1)

v3_2 = pya.Polygon([pya.Point(152, 120), pya.Point(224, 120), pya.Point(224, 192), pya.Point(152, 192)])
top_cell.shapes(v3_layer).insert(v3_2)

m4_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(m4_layer).insert(m4_1)

m4_2 = pya.Polygon([pya.Point(152, 120), pya.Point(224, 120), pya.Point(224, 192), pya.Point(152, 192)])
top_cell.shapes(m4_layer).insert(m4_2)

m3 = pya.Polygon([pya.Point(-20, -20), pya.Point(244, -20), pya.Point(244, 212), pya.Point(-20, 212)])
top_cell.shapes(m3_layer).insert(m3)

layout.write("../gds/Polygon277.gds")
