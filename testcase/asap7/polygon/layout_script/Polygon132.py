import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon132")


m6_layer = layout.layer(60, 0)

m6 = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 112), pya.Point(0, 112)])
top_cell.shapes(m6_layer).insert(m6)

layout.write("../gds/Polygon132.gds")
