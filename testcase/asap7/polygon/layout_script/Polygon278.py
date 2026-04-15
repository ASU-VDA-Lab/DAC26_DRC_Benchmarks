import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon278")


v3_layer = layout.layer(35, 0)
m4_layer = layout.layer(40, 0)

v3_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v3_layer).insert(v3_1)

m4_1 = pya.Polygon([ pya.Point(0, 0), pya.Point(20, 0), pya.Point(20, -20), pya.Point(52, -20), pya.Point(52, 0), pya.Point(72, 0), pya.Point(72, 20), pya.Point(92, 20), pya.Point(92, 52), pya.Point(72, 52), pya.Point(72, 72), pya.Point(52, 72), pya.Point(52, 92), pya.Point(20, 92), pya.Point(20, 72), pya.Point(0, 72), pya.Point(0, 52), pya.Point(-20, 52), pya.Point(-20, 20), pya.Point(0, 20), ])
top_cell.shapes(m4_layer).insert(m4_1)

v3_2 = pya.Polygon([pya.Point(128, 128), pya.Point(200, 128), pya.Point(200, 200), pya.Point(128, 200)])
top_cell.shapes(v3_layer).insert(v3_2)

m4_2 = pya.Polygon([pya.Point(128, 128), pya.Point(200, 128), pya.Point(200, 200), pya.Point(128, 200)])
top_cell.shapes(m4_layer).insert(m4_2)

layout.write("../gds/Polygon278.gds")
