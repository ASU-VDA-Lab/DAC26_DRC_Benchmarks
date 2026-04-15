import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon101")


m4_layer = layout.layer(40, 0)

m4_1 = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 288), pya.Point(0, 288)])
top_cell.shapes(m4_layer).insert(m4_1)

m4_2 = pya.Polygon([pya.Point(320, 320), pya.Point(512, 320), pya.Point(512, 608), pya.Point(320, 608)])
top_cell.shapes(m4_layer).insert(m4_2)

layout.write("../gds/Polygon101.gds")
