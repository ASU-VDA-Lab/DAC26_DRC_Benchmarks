import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon54")


lig_layer = layout.layer(16, 0)

lig1 = pya.Polygon([pya.Point(0, 0), pya.Point(120, 0), pya.Point(120, 120), pya.Point(0, 120)])
top_cell.shapes(lig_layer).insert(lig1)

lig2 = pya.Polygon([pya.Point(20, 232), pya.Point(100, 232), pya.Point(100, 312), pya.Point(20, 312)])
top_cell.shapes(lig_layer).insert(lig2)

layout.write("../gds/Polygon54.gds")
