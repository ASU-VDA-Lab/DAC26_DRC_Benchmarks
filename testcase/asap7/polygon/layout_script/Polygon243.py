import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon243")


v0_layer = layout.layer(18, 0)
m1_layer = layout.layer(19, 0)
lig_layer = layout.layer(16, 0)

v0 = pya.Polygon([pya.Point(0, 0), pya.Point(76, 0), pya.Point(76, 76), pya.Point(0, 76)])
top_cell.shapes(v0_layer).insert(v0)

lig = pya.Polygon([pya.Point(2, 2), pya.Point(74, 2), pya.Point(74, 74), pya.Point(2, 74)])
top_cell.shapes(lig_layer).insert(lig)

m1 = pya.Polygon([pya.Point(-20, -20), pya.Point(96, -20), pya.Point(96, 96), pya.Point(-20, 96)])
top_cell.shapes(m1_layer).insert(m1)

layout.write("../gds/Polygon243.gds")
