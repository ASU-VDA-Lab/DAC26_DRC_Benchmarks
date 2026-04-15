import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon273")


v3_layer = layout.layer(35, 0)
m3_layer = layout.layer(30, 0)
m4_layer = layout.layer(40, 0)

v3 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v3_layer).insert(v3)

m3 = pya.Polygon([pya.Point(-20, -20), pya.Point(92, -20), pya.Point(92, 92), pya.Point(-20, 92)])
top_cell.shapes(m3_layer).insert(m3)

m4 = pya.Polygon([pya.Point(-60, -44), pya.Point(132, -44), pya.Point(132, 116), pya.Point(-60, 116)])
top_cell.shapes(m4_layer).insert(m4)

layout.write("../gds/Polygon273.gds")
