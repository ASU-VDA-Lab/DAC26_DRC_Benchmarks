import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon260")


v1_layer = layout.layer(21, 0)
m2_layer = layout.layer(20, 0)

v1_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v1_layer).insert(v1_1)

m2_1 = pya.Polygon([ pya.Point(0, 0), pya.Point(20, 0), pya.Point(20, -20), pya.Point(52, -20), pya.Point(52, 0), pya.Point(72, 0), pya.Point(72, 20), pya.Point(92, 20), pya.Point(92, 52), pya.Point(72, 52), pya.Point(72, 72), pya.Point(52, 72), pya.Point(52, 92), pya.Point(20, 92), pya.Point(20, 72), pya.Point(0, 72), pya.Point(0, 52), pya.Point(-20, 52), pya.Point(-20, 20), pya.Point(0, 20), ])
top_cell.shapes(m2_layer).insert(m2_1)

v1_2 = pya.Polygon([pya.Point(128, 128), pya.Point(200, 128), pya.Point(200, 200), pya.Point(128, 200)])
top_cell.shapes(v1_layer).insert(v1_2)

m2_2 = pya.Polygon([pya.Point(128, 128), pya.Point(200, 128), pya.Point(200, 200), pya.Point(128, 200)])
top_cell.shapes(m2_layer).insert(m2_2)

layout.write("../gds/Polygon260.gds")
