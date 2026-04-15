import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon171")


m9_layer = layout.layer(90, 0)

m9_1 = pya.Polygon([pya.Point(0, 0), pya.Point(240, 0), pya.Point(240, 504), pya.Point(0, 504)])
top_cell.shapes(m9_layer).insert(m9_1)

m9_2 = pya.Polygon([pya.Point(440, 0), pya.Point(600, 0), pya.Point(600, 752), pya.Point(440, 752)])
top_cell.shapes(m9_layer).insert(m9_2)

layout.write("../gds/Polygon171.gds")
