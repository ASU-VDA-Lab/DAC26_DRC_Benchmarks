import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon24")


gate_layer = layout.layer(7, 0)

gate1 = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 216), pya.Point(0, 216)])
gate2 = pya.Polygon([pya.Point(0, 256), pya.Point(80, 256), pya.Point(80, 472), pya.Point(0, 472)])
gate3 = pya.Polygon([pya.Point(0, 512), pya.Point(80, 512), pya.Point(80, 728), pya.Point(0, 728)])
top_cell.shapes(gate_layer).insert(gate1)
top_cell.shapes(gate_layer).insert(gate2)
top_cell.shapes(gate_layer).insert(gate3)

layout.write("../gds/Polygon24.gds")
