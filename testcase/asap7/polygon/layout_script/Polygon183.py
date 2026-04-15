import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon183")


active_layer = layout.layer(11, 0)
gate_layer = layout.layer(7, 0)
nselect_layer = layout.layer(12, 0)

gate = pya.Polygon([pya.Point(200, 0), pya.Point(280, 0), pya.Point(280, 216), pya.Point(200, 216)])
top_cell.shapes(gate_layer).insert(gate)

active = pya.Polygon([pya.Point(80, 16), pya.Point(520, 16), pya.Point(520, 200), pya.Point(80, 200)])
top_cell.shapes(active_layer).insert(active)

nselect = pya.Polygon([pya.Point(180, -120), pya.Point(800, -120), pya.Point(800, 336), pya.Point(180, 336)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon183.gds")
