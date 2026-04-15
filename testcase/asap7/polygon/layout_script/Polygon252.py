import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon252")


v0_layer = layout.layer(18, 0)
m1_layer = layout.layer(19, 0)
lisd_layer = layout.layer(17, 0)

v0 = pya.Polygon([pya.Point(0, 0), pya.Point(64, 0), pya.Point(64, 72), pya.Point(0, 72)])
top_cell.shapes(v0_layer).insert(v0)

m1 = pya.Polygon([pya.Point(-20, -20), pya.Point(84, -20), pya.Point(84, 92), pya.Point(-20, 92)])
top_cell.shapes(m1_layer).insert(m1)

lisd = pya.Polygon([pya.Point(-20, -20), pya.Point(84, -20), pya.Point(84, 92), pya.Point(-20, 92)])
top_cell.shapes(lisd_layer).insert(lisd)

layout.write("../gds/Polygon252.gds")
