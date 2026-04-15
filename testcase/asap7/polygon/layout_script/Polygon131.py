import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon131")


m6_layer = layout.layer(60, 0)

m6_1a = pya.Polygon([pya.Point(0, 0), pya.Point(256, 0), pya.Point(256, 400), pya.Point(0, 400)])
top_cell.shapes(m6_layer).insert(m6_1a)

m6_1b = pya.Polygon([pya.Point(128, 496), pya.Point(384, 496), pya.Point(384, 896), pya.Point(128, 896)])
top_cell.shapes(m6_layer).insert(m6_1b)

m6_2a = pya.Polygon([pya.Point(0, 1280), pya.Point(256, 1280), pya.Point(256, 1680), pya.Point(0, 1680)])
top_cell.shapes(m6_layer).insert(m6_2a)

m6_2b = pya.Polygon([pya.Point(128, 1808), pya.Point(384, 1808), pya.Point(384, 2208), pya.Point(128, 2208)])
top_cell.shapes(m6_layer).insert(m6_2b)

layout.write("../gds/Polygon131.gds")
