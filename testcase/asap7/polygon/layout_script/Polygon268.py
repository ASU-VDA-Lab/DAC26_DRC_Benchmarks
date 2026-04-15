import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon268")


v2_layer = layout.layer(25, 0)
m2_layer = layout.layer(20, 0)
m3_layer = layout.layer(30, 0)

v2_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v2_layer).insert(v2_1)

v2_2 = pya.Polygon([pya.Point(152, 120), pya.Point(224, 120), pya.Point(224, 192), pya.Point(152, 192)])
top_cell.shapes(v2_layer).insert(v2_2)

m3_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(m3_layer).insert(m3_1)

m3_2 = pya.Polygon([pya.Point(152, 120), pya.Point(224, 120), pya.Point(224, 192), pya.Point(152, 192)])
top_cell.shapes(m3_layer).insert(m3_2)

m2 = pya.Polygon([pya.Point(-20, -20), pya.Point(244, -20), pya.Point(244, 212), pya.Point(-20, 212)])
top_cell.shapes(m2_layer).insert(m2)

layout.write("../gds/Polygon268.gds")
