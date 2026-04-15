import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon136")


m6_layer = layout.layer(60, 0)

m6 = pya.Polygon([pya.Point(0, 0), pya.Point(160, 0), pya.Point(160, 128), pya.Point(0, 128)])
top_cell.shapes(m6_layer).insert(m6)

layout.write("../gds/Polygon136.gds")
