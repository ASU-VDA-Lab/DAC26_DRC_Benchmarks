import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon48")


lig_layer = layout.layer(16, 0)
lisd_layer = layout.layer(17, 0)

lig = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 200), pya.Point(0, 200)])
top_cell.shapes(lig_layer).insert(lig)

lisd = pya.Polygon([pya.Point(120, 0), pya.Point(240, 0), pya.Point(240, 200), pya.Point(120, 200)])
top_cell.shapes(lisd_layer).insert(lisd)

layout.write("../gds/Polygon48.gds")
