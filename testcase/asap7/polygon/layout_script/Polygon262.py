import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon262")


v2_layer = layout.layer(25, 0)
m2_layer = layout.layer(20, 0)
m3_layer = layout.layer(30, 0)

v2 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v2_layer).insert(v2)

m2 = pya.Polygon([pya.Point(20, -20), pya.Point(100, -20), pya.Point(100, 100), pya.Point(20, 100)])
top_cell.shapes(m2_layer).insert(m2)

m3 = pya.Polygon([pya.Point(-20, -20), pya.Point(92, -20), pya.Point(92, 92), pya.Point(-20, 92)])
top_cell.shapes(m3_layer).insert(m3)

layout.write("../gds/Polygon262.gds")
