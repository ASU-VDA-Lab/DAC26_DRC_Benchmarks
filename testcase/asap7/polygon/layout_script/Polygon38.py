import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon38")


lig_layer = layout.layer(16, 0)

lig = pya.Polygon([pya.Point(0, 0), pya.Point(64, 0), pya.Point(64, 72), pya.Point(0, 72)])
top_cell.shapes(lig_layer).insert(lig)

layout.write("../gds/Polygon38.gds")
