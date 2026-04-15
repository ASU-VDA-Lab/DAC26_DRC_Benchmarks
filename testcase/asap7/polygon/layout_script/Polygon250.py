import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon250")


v0_layer = layout.layer(18, 0)
m1_layer = layout.layer(19, 0)
lisd_layer = layout.layer(17, 0)

v0_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v0_layer).insert(v0_1)

v0_2 = pya.Polygon([pya.Point(152, 120), pya.Point(224, 120), pya.Point(224, 192), pya.Point(152, 192)])
top_cell.shapes(v0_layer).insert(v0_2)

m1_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(m1_layer).insert(m1_1)

m1_2 = pya.Polygon([pya.Point(152, 120), pya.Point(224, 120), pya.Point(224, 192), pya.Point(152, 192)])
top_cell.shapes(m1_layer).insert(m1_2)

lisd = pya.Polygon([pya.Point(-20, -20), pya.Point(244, -20), pya.Point(244, 212), pya.Point(-20, 212)])
top_cell.shapes(lisd_layer).insert(lisd)

layout.write("../gds/Polygon250.gds")
