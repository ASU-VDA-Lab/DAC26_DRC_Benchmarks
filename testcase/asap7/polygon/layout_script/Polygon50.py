import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon50")


lig_layer = layout.layer(16, 0)

lig1 = pya.Polygon([pya.Point(0, 0), pya.Point(200, 0), pya.Point(200, 200), pya.Point(0, 200)])
top_cell.shapes(lig_layer).insert(lig1)

lig2 = pya.Polygon([pya.Point(256, 0), pya.Point(456, 0), pya.Point(456, 200), pya.Point(256, 200)])
top_cell.shapes(lig_layer).insert(lig2)

layout.write("../gds/Polygon50.gds")
