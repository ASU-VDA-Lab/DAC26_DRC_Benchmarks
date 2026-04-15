import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon121")


m5_layer = layout.layer(50, 0)

m5 = pya.Polygon([pya.Point(0, 0), pya.Point(288, 0), pya.Point(288, 192), pya.Point(0, 192)])
top_cell.shapes(m5_layer).insert(m5)

layout.write("../gds/Polygon121.gds")
