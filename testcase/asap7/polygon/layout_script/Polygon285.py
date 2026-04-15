import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon285")


v4_layer = layout.layer(45, 0)
m4_layer = layout.layer(40, 0)
m5_layer = layout.layer(50, 0)

v4_1 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 96), pya.Point(0, 96)])
top_cell.shapes(v4_layer).insert(v4_1)

v4_2 = pya.Polygon([pya.Point(208, 0), pya.Point(304, 0), pya.Point(304, 96), pya.Point(208, 96)])
top_cell.shapes(v4_layer).insert(v4_2)

m4_1 = pya.Polygon([pya.Point(-80, -80), pya.Point(176, -80), pya.Point(176, 400), pya.Point(-80, 400)])
top_cell.shapes(m4_layer).insert(m4_1)

m4_2 = pya.Polygon([pya.Point(208, -80), pya.Point(480, -80), pya.Point(480, 400), pya.Point(208, 400)])
top_cell.shapes(m4_layer).insert(m4_2)

m5_1 = pya.Polygon([pya.Point(-80, -80), pya.Point(176, -80), pya.Point(176, 400), pya.Point(-80, 400)])
top_cell.shapes(m5_layer).insert(m5_1)

m5_2 = pya.Polygon([pya.Point(208, -80), pya.Point(480, -80), pya.Point(480, 400), pya.Point(208, 400)])
top_cell.shapes(m5_layer).insert(m5_2)

layout.write("../gds/Polygon285.gds")
