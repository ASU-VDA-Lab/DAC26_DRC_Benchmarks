import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon25")


gate_layer = layout.layer(7, 0)
gate1 = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 216), pya.Point(0, 216)])
gate2 = pya.Polygon([pya.Point(240, 0), pya.Point(320, 0), pya.Point(320, 216), pya.Point(240, 216)])
top_cell.shapes(gate_layer).insert(gate1)
top_cell.shapes(gate_layer).insert(gate2)

layout.write("../gds/Polygon25.gds")
