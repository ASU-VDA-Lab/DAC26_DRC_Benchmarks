import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon44")


lig_layer = layout.layer(16, 0)
gate_layer = layout.layer(7, 0)

gate = pya.Polygon([pya.Point(200, 0), pya.Point(280, 0), pya.Point(280, 216), pya.Point(200, 216)])
top_cell.shapes(gate_layer).insert(gate)

lig = pya.Polygon([pya.Point(320, 40), pya.Point(400, 40), pya.Point(400, 176), pya.Point(320, 176)])
top_cell.shapes(lig_layer).insert(lig)

layout.write("../gds/Polygon44.gds")
