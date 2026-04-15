import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon129")


m6_layer = layout.layer(60, 0)

m6_1 = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 384), pya.Point(0, 384)])
top_cell.shapes(m6_layer).insert(m6_1)

m6_2 = pya.Polygon([pya.Point(320, 416), pya.Point(512, 416), pya.Point(512, 800), pya.Point(320, 800)])
top_cell.shapes(m6_layer).insert(m6_2)

layout.write("../gds/Polygon129.gds")
