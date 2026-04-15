import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon274")


v3_layer = layout.layer(35, 0)
m3_layer = layout.layer(30, 0)
m4_layer = layout.layer(40, 0)

v3 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v3_layer).insert(v3)

m3 = pya.Polygon([pya.Point(-44, -44), pya.Point(800, -44), pya.Point(800, 800), pya.Point(-44, 800)])
top_cell.shapes(m3_layer).insert(m3)

m4 = pya.Polygon([pya.Point(-20, -20), pya.Point(800, -20), pya.Point(800, 800), pya.Point(-20, 800)])
top_cell.shapes(m4_layer).insert(m4)

layout.write("../gds/Polygon274.gds")
