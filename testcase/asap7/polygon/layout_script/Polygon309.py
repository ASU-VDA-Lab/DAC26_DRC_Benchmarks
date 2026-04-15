import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon309")


v7_layer = layout.layer(75, 0)
m7_layer = layout.layer(70, 0)
m8_layer = layout.layer(80, 0)

v7_1 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 96), pya.Point(0, 96)])
top_cell.shapes(v7_layer).insert(v7_1)

v7_2 = pya.Polygon([pya.Point(256, 0), pya.Point(352, 0), pya.Point(352, 96), pya.Point(256, 96)])
top_cell.shapes(v7_layer).insert(v7_2)

m7_1 = pya.Polygon([pya.Point(-60, -60), pya.Point(156, -60), pya.Point(156, 300), pya.Point(-60, 300)])
top_cell.shapes(m7_layer).insert(m7_1)

m7_2 = pya.Polygon([pya.Point(196, -60), pya.Point(412, -60), pya.Point(412, 300), pya.Point(196, 300)])
top_cell.shapes(m7_layer).insert(m7_2)

m8_1 = pya.Polygon([pya.Point(-60, -60), pya.Point(156, -60), pya.Point(156, 300), pya.Point(-60, 300)])
top_cell.shapes(m8_layer).insert(m8_1)

m8_2 = pya.Polygon([pya.Point(196, -60), pya.Point(412, -60), pya.Point(412, 300), pya.Point(196, 300)])
top_cell.shapes(m8_layer).insert(m8_2)

layout.write("../gds/Polygon309.gds")
