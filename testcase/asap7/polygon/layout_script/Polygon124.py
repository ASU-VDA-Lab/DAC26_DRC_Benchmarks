import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon124")


m6_layer = layout.layer(60, 0)

m6_valid = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 128), pya.Point(0, 128)])
top_cell.shapes(m6_layer).insert(m6_valid)

m6_offtrack = pya.Polygon([pya.Point(0, 384), pya.Point(192, 384), pya.Point(192, 512), pya.Point(0, 512)])
top_cell.shapes(m6_layer).insert(m6_offtrack)

layout.write("../gds/Polygon124.gds")
