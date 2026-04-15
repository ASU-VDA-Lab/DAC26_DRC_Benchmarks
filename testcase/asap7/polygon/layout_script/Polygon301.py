import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon301")


v6_layer = layout.layer(65, 0)
m6_layer = layout.layer(60, 0)
m7_layer = layout.layer(70, 0)

v6_1 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 96), pya.Point(0, 96)])
top_cell.shapes(v6_layer).insert(v6_1)

v6_2 = pya.Polygon([pya.Point(256, 0), pya.Point(352, 0), pya.Point(352, 96), pya.Point(256, 96)])
top_cell.shapes(v6_layer).insert(v6_2)

m6_1 = pya.Polygon([pya.Point(-60, -60), pya.Point(156, -60), pya.Point(156, 300), pya.Point(-60, 300)])
top_cell.shapes(m6_layer).insert(m6_1)

m6_2 = pya.Polygon([pya.Point(196, -60), pya.Point(412, -60), pya.Point(412, 300), pya.Point(196, 300)])
top_cell.shapes(m6_layer).insert(m6_2)

m7_1 = pya.Polygon([pya.Point(-60, -60), pya.Point(156, -60), pya.Point(156, 300), pya.Point(-60, 300)])
top_cell.shapes(m7_layer).insert(m7_1)

m7_2 = pya.Polygon([pya.Point(196, -60), pya.Point(412, -60), pya.Point(412, 300), pya.Point(196, 300)])
top_cell.shapes(m7_layer).insert(m7_2)

layout.write("../gds/Polygon301.gds")
