import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon244")


v0_layer = layout.layer(18, 0)
m1_layer = layout.layer(19, 0)
lisd_layer = layout.layer(17, 0)

v0 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v0_layer).insert(v0)

lisd = pya.Polygon([pya.Point(-4, -4), pya.Point(92, -4), pya.Point(92, 104), pya.Point(-4, 104)])
top_cell.shapes(lisd_layer).insert(lisd)

m1 = pya.Polygon([pya.Point(-20, -20), pya.Point(92, -20), pya.Point(92, 92), pya.Point(-20, 92)])
top_cell.shapes(m1_layer).insert(m1)

layout.write("../gds/Polygon244.gds")
