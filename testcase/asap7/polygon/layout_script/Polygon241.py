import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon241")


v0_layer = layout.layer(18, 0)
m1_layer = layout.layer(19, 0)
lig_layer = layout.layer(16, 0)

v0 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v0_layer).insert(v0)

m1 = pya.Polygon([pya.Point(-20, -20), pya.Point(92, -20), pya.Point(92, 92), pya.Point(-20, 92)])
top_cell.shapes(m1_layer).insert(m1)

lig = pya.Polygon([pya.Point(20, 20), pya.Point(100, 20), pya.Point(100, 100), pya.Point(20, 100)])
top_cell.shapes(lig_layer).insert(lig)

layout.write("../gds/Polygon241.gds")
