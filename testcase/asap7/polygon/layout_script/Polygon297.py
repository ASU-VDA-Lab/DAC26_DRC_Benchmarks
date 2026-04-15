import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon297")


v6_layer = layout.layer(65, 0)
m6_layer = layout.layer(60, 0)
m7_layer = layout.layer(70, 0)

v6 = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 96), pya.Point(0, 96)])
top_cell.shapes(v6_layer).insert(v6)

m6 = pya.Polygon([pya.Point(-20, -20), pya.Point(800, -20), pya.Point(800, 800), pya.Point(-20, 800)])
top_cell.shapes(m6_layer).insert(m6)

m7 = pya.Polygon([pya.Point(-44, -44), pya.Point(800, -44), pya.Point(800, 800), pya.Point(-44, 800)])
top_cell.shapes(m7_layer).insert(m7)

layout.write("../gds/Polygon297.gds")
