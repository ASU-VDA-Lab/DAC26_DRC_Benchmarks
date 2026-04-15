import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon52")


lig_layer = layout.layer(16, 0)

lig1 = pya.Polygon([pya.Point(0, 0), pya.Point(120, 0), pya.Point(120, 120), pya.Point(0, 120)])
top_cell.shapes(lig_layer).insert(lig1)

lig2 = pya.Polygon([pya.Point(0, 220), pya.Point(120, 220), pya.Point(120, 340), pya.Point(0, 340)])
top_cell.shapes(lig_layer).insert(lig2)

layout.write("../gds/Polygon52.gds")
