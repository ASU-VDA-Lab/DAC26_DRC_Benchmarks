import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon148")


m7_layer = layout.layer(70, 0)

m7 = pya.Polygon([pya.Point(0, 0), pya.Point(256, 0), pya.Point(256, 192), pya.Point(0, 192)])
top_cell.shapes(m7_layer).insert(m7)

layout.write("../gds/Polygon148.gds")
