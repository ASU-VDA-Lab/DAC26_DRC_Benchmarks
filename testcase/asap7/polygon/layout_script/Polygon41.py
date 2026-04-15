import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon41")


lig_layer = layout.layer(16, 0)
gate_layer = layout.layer(7, 0)

gate = pya.Polygon([pya.Point(200, 0), pya.Point(280, 0), pya.Point(280, 216), pya.Point(200, 216)])
top_cell.shapes(gate_layer).insert(gate)

lig = pya.Polygon([pya.Point(198, -40), pya.Point(282, -40), pya.Point(282, 256), pya.Point(198, 256)])
top_cell.shapes(lig_layer).insert(lig)

layout.write("../gds/Polygon41.gds")
