import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon190")


active_layer = layout.layer(11, 0)
gate_layer = layout.layer(7, 0)
pselect_layer = layout.layer(13, 0)
nwell_layer = layout.layer(1, 0)

gate = pya.Polygon([pya.Point(200, 0), pya.Point(280, 0), pya.Point(280, 216), pya.Point(200, 216)])
top_cell.shapes(gate_layer).insert(gate)

active = pya.Polygon([pya.Point(80, 16), pya.Point(520, 16), pya.Point(520, 200), pya.Point(80, 200)])
top_cell.shapes(active_layer).insert(active)

nwell = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 240), pya.Point(0, 240)])
top_cell.shapes(nwell_layer).insert(nwell)

pselect = pya.Polygon([pya.Point(180, -120), pya.Point(800, -120), pya.Point(800, 336), pya.Point(180, 336)])
top_cell.shapes(pselect_layer).insert(pselect)

layout.write("../gds/Polygon190.gds")
