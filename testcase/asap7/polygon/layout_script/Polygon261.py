import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon261")


v1_layer = layout.layer(21, 0)
m1_layer = layout.layer(19, 0)
m2_layer = layout.layer(20, 0)

v1 = pya.Polygon([pya.Point(0, 0), pya.Point(64, 0), pya.Point(64, 72), pya.Point(0, 72)])
top_cell.shapes(v1_layer).insert(v1)

m1 = pya.Polygon([pya.Point(-20, -20), pya.Point(84, -20), pya.Point(84, 92), pya.Point(-20, 92)])
top_cell.shapes(m1_layer).insert(m1)

m2 = pya.Polygon([pya.Point(-20, -20), pya.Point(84, -20), pya.Point(84, 92), pya.Point(-20, 92)])
top_cell.shapes(m2_layer).insert(m2)

layout.write("../gds/Polygon261.gds")
