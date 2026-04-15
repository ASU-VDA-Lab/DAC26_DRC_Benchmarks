import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon27")


gate_layer = layout.layer(7, 0)
gate = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 216), pya.Point(0, 216)])
top_cell.shapes(gate_layer).insert(gate)

layout.write("../gds/Polygon27.gds")
