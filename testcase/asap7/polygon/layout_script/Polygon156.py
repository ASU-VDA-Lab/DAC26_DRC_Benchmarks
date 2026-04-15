import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon156")


m8_layer = layout.layer(80, 0)

m8_1 = pya.Polygon([pya.Point(0, 0), pya.Point(316, 0), pya.Point(316, 384), pya.Point(0, 384)])
top_cell.shapes(m8_layer).insert(m8_1)

m8_2 = pya.Polygon([pya.Point(516, 0), pya.Point(832, 0), pya.Point(832, 384), pya.Point(516, 384)])
top_cell.shapes(m8_layer).insert(m8_2)

layout.write("../gds/Polygon156.gds")
