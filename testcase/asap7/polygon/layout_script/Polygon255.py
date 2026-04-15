import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon255")


v1_layer = layout.layer(21, 0)
m1_layer = layout.layer(19, 0)
m2_layer = layout.layer(20, 0)

v1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v1_layer).insert(v1)

m1 = pya.Polygon([pya.Point(-20, -20), pya.Point(92, -20), pya.Point(92, 92), pya.Point(-20, 92)])
top_cell.shapes(m1_layer).insert(m1)

m2 = pya.Polygon([pya.Point(-20, -20), pya.Point(100, -20), pya.Point(100, 120), pya.Point(-20, 120)])
top_cell.shapes(m2_layer).insert(m2)

layout.write("../gds/Polygon255.gds")
