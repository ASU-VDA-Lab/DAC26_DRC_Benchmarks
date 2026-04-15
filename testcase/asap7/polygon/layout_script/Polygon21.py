import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon21")


gate_layer = layout.layer(7, 0)
active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)

gate = pya.Polygon([pya.Point(120, 0), pya.Point(200, 0), pya.Point(200, 216), pya.Point(120, 216)])
active = pya.Polygon([pya.Point(40, 16), pya.Point(480, 16), pya.Point(480, 200), pya.Point(40, 200)])
nselect = pya.Polygon([pya.Point(-160, -120), pya.Point(720, -120), pya.Point(720, 336), pya.Point(-160, 336)])

top_cell.shapes(gate_layer).insert(gate)
top_cell.shapes(active_layer).insert(active)
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon21.gds")
