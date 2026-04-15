import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon9")


active_layer = layout.layer(11, 0)
fin_layer = layout.layer(2, 0)
gate_layer = layout.layer(7, 0)
nselect_layer = layout.layer(12, 0)

active_1 = pya.Polygon([pya.Point(0, 16), pya.Point(216, 16), pya.Point(216, 232), pya.Point(0, 232)])
top_cell.shapes(active_layer).insert(active_1)

active_2 = pya.Polygon([pya.Point(336, 16), pya.Point(552, 16), pya.Point(552, 232), pya.Point(336, 232)])
top_cell.shapes(active_layer).insert(active_2)

fin = pya.Polygon([pya.Point(-80, 96), pya.Point(632, 96), pya.Point(632, 124), pya.Point(-80, 124)])
top_cell.shapes(fin_layer).insert(fin)

gate = pya.Polygon([pya.Point(32, -40), pya.Point(112, -40), pya.Point(112, 288), pya.Point(32, 288)])
top_cell.shapes(gate_layer).insert(gate)
gate = pya.Polygon([pya.Point(136, -40), pya.Point(216, -40), pya.Point(216, 288), pya.Point(136, 288)])
top_cell.shapes(gate_layer).insert(gate)
gate = pya.Polygon([pya.Point(336, -40), pya.Point(416, -40), pya.Point(416, 288), pya.Point(336, 288)])
top_cell.shapes(gate_layer).insert(gate)
gate = pya.Polygon([pya.Point(440, -40), pya.Point(520, -40), pya.Point(520, 288), pya.Point(440, 288)])
top_cell.shapes(gate_layer).insert(gate)

nselect = pya.Polygon([pya.Point(-200, -160), pya.Point(760, -160), pya.Point(760, 392), pya.Point(-200, 392)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon9.gds")
