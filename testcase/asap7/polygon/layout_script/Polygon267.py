import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon267")


v2_layer = layout.layer(25, 0)
m3_layer = layout.layer(30, 0)

v2_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v2_layer).insert(v2_1)

m3_1 = pya.Polygon([ pya.Point(0, 0), pya.Point(20, 0), pya.Point(20, -20), pya.Point(52, -20), pya.Point(52, 0), pya.Point(72, 0), pya.Point(72, 20), pya.Point(92, 20), pya.Point(92, 52), pya.Point(72, 52), pya.Point(72, 72), pya.Point(52, 72), pya.Point(52, 92), pya.Point(20, 92), pya.Point(20, 72), pya.Point(0, 72), pya.Point(0, 52), pya.Point(-20, 52), pya.Point(-20, 20), pya.Point(0, 20), ])
top_cell.shapes(m3_layer).insert(m3_1)

v2_2 = pya.Polygon([pya.Point(128, 128), pya.Point(200, 128), pya.Point(200, 200), pya.Point(128, 200)])
top_cell.shapes(v2_layer).insert(v2_2)

m3_2 = pya.Polygon([ pya.Point(128, 128), pya.Point(148, 128), pya.Point(148, 108), pya.Point(180, 108), pya.Point(180, 128), pya.Point(200, 128), pya.Point(200, 148), pya.Point(220, 148), pya.Point(220, 180), pya.Point(200, 180), pya.Point(200, 200), pya.Point(180, 200), pya.Point(180, 220), pya.Point(148, 220), pya.Point(148, 200), pya.Point(128, 200), pya.Point(128, 180), pya.Point(108, 180), pya.Point(108, 148), pya.Point(128, 148), ])
top_cell.shapes(m3_layer).insert(m3_2)

layout.write("../gds/Polygon267.gds")
