import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon57")


lisd_layer = layout.layer(17, 0)

lisd = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 100), pya.Point(0, 100)])
top_cell.shapes(lisd_layer).insert(lisd)

layout.write("../gds/Polygon57.gds")
