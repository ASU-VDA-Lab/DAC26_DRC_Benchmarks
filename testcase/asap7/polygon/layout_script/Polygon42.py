import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon42")

gate_layer = layout.layer(7, 0)
gcut_layer = layout.layer(10, 0)
active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
lig_layer = layout.layer(16, 0)

active = pya.Polygon([pya.Point(40, 0), pya.Point(600, 0), pya.Point(600, 216), pya.Point(40, 216)])
top_cell.shapes(active_layer).insert(active)

gate1 = pya.Polygon([pya.Point(160, -80), pya.Point(240, -80), pya.Point(240, 400), pya.Point(160, 400)])
top_cell.shapes(gate_layer).insert(gate1)

gate2 = pya.Polygon([pya.Point(400, -80), pya.Point(480, -80), pya.Point(480, 400), pya.Point(400, 400)])
top_cell.shapes(gate_layer).insert(gate2)

lig = pya.Polygon([pya.Point(80, 228), pya.Point(320, 228), pya.Point(320, 340), pya.Point(80, 340)])
top_cell.shapes(lig_layer).insert(lig)

gcut = pya.Polygon([pya.Point(100, 420), pya.Point(380, 420), pya.Point(380, 520), pya.Point(100, 520)])
top_cell.shapes(gcut_layer).insert(gcut)

nselect = pya.Polygon([pya.Point(-120, -200), pya.Point(720, -200), pya.Point(720, 360), pya.Point(-120, 360)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon42.gds")