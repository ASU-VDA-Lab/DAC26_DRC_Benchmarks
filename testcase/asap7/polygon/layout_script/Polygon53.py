import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon53")


lig_layer = layout.layer(16, 0)

lig1 = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 80), pya.Point(0, 80)])
top_cell.shapes(lig_layer).insert(lig1)

lig2 = pya.Polygon([pya.Point(0, 192), pya.Point(80, 192), pya.Point(80, 272), pya.Point(0, 272)])
top_cell.shapes(lig_layer).insert(lig2)

layout.write("../gds/Polygon53.gds")
