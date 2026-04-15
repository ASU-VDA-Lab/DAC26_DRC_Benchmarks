import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon279")


v3_layer = layout.layer(35, 0)
m3_layer = layout.layer(30, 0)
m4_layer = layout.layer(40, 0)

v3 = pya.Polygon([pya.Point(0, 0), pya.Point(64, 0), pya.Point(64, 72), pya.Point(0, 72)])
top_cell.shapes(v3_layer).insert(v3)

m3 = pya.Polygon([pya.Point(-20, -20), pya.Point(84, -20), pya.Point(84, 92), pya.Point(-20, 92)])
top_cell.shapes(m3_layer).insert(m3)

m4 = pya.Polygon([pya.Point(-64, -12), pya.Point(128, -12), pya.Point(128, 84), pya.Point(-64, 84)])
top_cell.shapes(m4_layer).insert(m4)

layout.write("../gds/Polygon279.gds")
