import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon165")


m8_layer = layout.layer(80, 0)

m8 = pya.Polygon([pya.Point(0, 0), pya.Point(8400, 0), pya.Point(8400, 8400), pya.Point(0, 8400)])
top_cell.shapes(m8_layer).insert(m8)

layout.write("../gds/Polygon165.gds")
