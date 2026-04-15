import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon45")


lig_layer = layout.layer(16, 0)
gate_layer = layout.layer(7, 0)
gcut_layer = layout.layer(10, 0)

gate = pya.Polygon([pya.Point(200, 0), pya.Point(280, 0), pya.Point(280, 400), pya.Point(200, 400)])
top_cell.shapes(gate_layer).insert(gate)

gcut = pya.Polygon([pya.Point(120, 160), pya.Point(360, 160), pya.Point(360, 240), pya.Point(120, 240)])
top_cell.shapes(gcut_layer).insert(gcut)

lig = pya.Polygon([pya.Point(120, 252), pya.Point(200, 252), pya.Point(200, 332), pya.Point(120, 332)])
top_cell.shapes(lig_layer).insert(lig)

layout.write("../gds/Polygon45.gds")
