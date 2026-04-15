import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon133")


m6_layer = layout.layer(60, 0)

m6 = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 2640), pya.Point(0, 2640)])
top_cell.shapes(m6_layer).insert(m6)

layout.write("../gds/Polygon133.gds")
