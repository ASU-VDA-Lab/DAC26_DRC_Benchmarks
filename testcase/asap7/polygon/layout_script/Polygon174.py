import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon174")


m9_layer = layout.layer(90, 0)

m9_1 = pya.Polygon([pya.Point(0, 0), pya.Point(2400, 0), pya.Point(2400, 2400), pya.Point(0, 2400)])
top_cell.shapes(m9_layer).insert(m9_1)

m9_2 = pya.Polygon([pya.Point(4200, 0), pya.Point(6600, 0), pya.Point(6600, 2400), pya.Point(4200, 2400)])
top_cell.shapes(m9_layer).insert(m9_2)

layout.write("../gds/Polygon174.gds")
