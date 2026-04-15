import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon218")


lig_layer = layout.layer(16, 0)
gate_layer = layout.layer(7, 0)
sramdrc_layer = layout.layer(99, 0)

gate = pya.Polygon([pya.Point(200, 0), pya.Point(280, 0), pya.Point(280, 216), pya.Point(200, 216)])
top_cell.shapes(gate_layer).insert(gate)

lig = pya.Polygon([pya.Point(240, 88), pya.Point(320, 88), pya.Point(320, 120), pya.Point(240, 120)])
top_cell.shapes(lig_layer).insert(lig)

sramdrc = pya.Polygon([pya.Point(160, -40), pya.Point(400, -40), pya.Point(400, 256), pya.Point(160, 256)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

layout.write("../gds/Polygon218.gds")
