import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon31")


gcut_layer = layout.layer(10, 0)
gcut = pya.Polygon([pya.Point(0, 0), pya.Point(200, 0), pya.Point(200, 80), pya.Point(0, 80)])
top_cell.shapes(gcut_layer).insert(gcut)

layout.write("../gds/Polygon31.gds")
