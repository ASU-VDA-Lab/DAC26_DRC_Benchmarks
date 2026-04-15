import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon15")


fin_layer = layout.layer(2, 0)


poly = pya.Polygon([ pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 28), pya.Point(428, 28), pya.Point(428, 108), pya.Point(400, 108), pya.Point(400, 28), pya.Point(0, 28), ])
top_cell.shapes(fin_layer).insert(poly)

layout.write("../gds/Polygon15.gds")
