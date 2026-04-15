import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon328")


nwell_layer = layout.layer(1, 0)
gate_layer = layout.layer(7, 0)

nwell = pya.Polygon([pya.Point(0, -12), pya.Point(800, -12), pya.Point(800, 800), pya.Point(0, 800)])
gate = pya.Polygon([pya.Point(200, 0), pya.Point(280, 0), pya.Point(280, 216), pya.Point(200, 216)])

top_cell.shapes(nwell_layer).insert(nwell)
top_cell.shapes(gate_layer).insert(gate)

layout.write("../gds/Polygon328.gds")
