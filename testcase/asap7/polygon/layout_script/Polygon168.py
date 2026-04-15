import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon168")


m9_layer = layout.layer(90, 0)

m9_1 = pya.Polygon([pya.Point(0, 0), pya.Point(160, 0), pya.Point(160, 400), pya.Point(0, 400)])
top_cell.shapes(m9_layer).insert(m9_1)

m9_2 = pya.Polygon([pya.Point(280, 0), pya.Point(440, 0), pya.Point(440, 400), pya.Point(280, 400)])
top_cell.shapes(m9_layer).insert(m9_2)

layout.write("../gds/Polygon168.gds")
