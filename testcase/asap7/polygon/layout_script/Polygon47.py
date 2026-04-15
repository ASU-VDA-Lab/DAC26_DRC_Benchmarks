import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon47")


lig_layer = layout.layer(16, 0)
lisd_layer = layout.layer(17, 0)

lig = pya.Polygon([pya.Point(0, 0), pya.Point(200, 0), pya.Point(200, 200), pya.Point(0, 200)])
top_cell.shapes(lig_layer).insert(lig)

lisd = pya.Polygon([pya.Point(184, 88), pya.Point(400, 88), pya.Point(400, 116), pya.Point(184, 116)])
top_cell.shapes(lisd_layer).insert(lisd)

layout.write("../gds/Polygon47.gds")
