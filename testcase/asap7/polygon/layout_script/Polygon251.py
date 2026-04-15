import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon251")


v0_layer = layout.layer(18, 0)
m1_layer = layout.layer(19, 0)
lisd_layer = layout.layer(17, 0)

v0_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v0_layer).insert(v0_1)

m1_1 = pya.Polygon([ pya.Point(0, 0), pya.Point(20, 0), pya.Point(20, -20), pya.Point(52, -20), pya.Point(52, 0), pya.Point(72, 0), pya.Point(72, 20), pya.Point(92, 20), pya.Point(92, 52), pya.Point(72, 52), pya.Point(72, 72), pya.Point(52, 72), pya.Point(52, 92), pya.Point(20, 92), pya.Point(20, 72), pya.Point(0, 72), pya.Point(0, 52), pya.Point(-20, 52), pya.Point(-20, 20), pya.Point(0, 20), ])
top_cell.shapes(m1_layer).insert(m1_1)

v0_2 = pya.Polygon([pya.Point(128, 128), pya.Point(200, 128), pya.Point(200, 200), pya.Point(128, 200)])
top_cell.shapes(v0_layer).insert(v0_2)

m1_2 = pya.Polygon([pya.Point(128, 128), pya.Point(200, 128), pya.Point(200, 200), pya.Point(128, 200)])
top_cell.shapes(m1_layer).insert(m1_2)

lisd = pya.Polygon([pya.Point(-40, -40), pya.Point(240, -40), pya.Point(240, 240), pya.Point(-40, 240)])
top_cell.shapes(lisd_layer).insert(lisd)

layout.write("../gds/Polygon251.gds")
