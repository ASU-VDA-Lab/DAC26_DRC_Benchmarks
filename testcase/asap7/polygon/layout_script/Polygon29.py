import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon29")


gate_layer = layout.layer(7, 0)
gate = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 140), pya.Point(0, 140)])
top_cell.shapes(gate_layer).insert(gate)

layout.write("../gds/Polygon29.gds")
