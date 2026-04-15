import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon28")


gate_layer = layout.layer(7, 0)
gate = pya.Polygon([pya.Point(0, 0), pya.Point(100, 0), pya.Point(100, 216), pya.Point(0, 216)])
top_cell.shapes(gate_layer).insert(gate)

layout.write("../gds/Polygon28.gds")
