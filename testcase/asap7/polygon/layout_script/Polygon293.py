import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon293")


v5_layer = layout.layer(55, 0)
m5_layer = layout.layer(50, 0)
m6_layer = layout.layer(60, 0)

v5_1 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 96), pya.Point(0, 96)])
top_cell.shapes(v5_layer).insert(v5_1)

v5_2 = pya.Polygon([pya.Point(208, 0), pya.Point(304, 0), pya.Point(304, 96), pya.Point(208, 96)])
top_cell.shapes(v5_layer).insert(v5_2)

m5_1 = pya.Polygon([pya.Point(-80, -80), pya.Point(176, -80), pya.Point(176, 400), pya.Point(-80, 400)])
top_cell.shapes(m5_layer).insert(m5_1)

m5_2 = pya.Polygon([pya.Point(208, -80), pya.Point(480, -80), pya.Point(480, 400), pya.Point(208, 400)])
top_cell.shapes(m5_layer).insert(m5_2)

m6_1 = pya.Polygon([pya.Point(-80, -80), pya.Point(176, -80), pya.Point(176, 400), pya.Point(-80, 400)])
top_cell.shapes(m6_layer).insert(m6_1)

m6_2 = pya.Polygon([pya.Point(208, -80), pya.Point(480, -80), pya.Point(480, 400), pya.Point(208, 400)])
top_cell.shapes(m6_layer).insert(m6_2)

layout.write("../gds/Polygon293.gds")
