import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon23")


gate_layer = layout.layer(7, 0)


poly = pya.Polygon([ pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 160), pya.Point(160, 160), pya.Point(160, 216), pya.Point(0, 216), ])
top_cell.shapes(gate_layer).insert(poly)

layout.write("../gds/Polygon23.gds")
