import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon20")


gate_layer = layout.layer(7, 0)
active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)

gate = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 216), pya.Point(0, 216)])
active = pya.Polygon([pya.Point(-100, 12), pya.Point(280, 12), pya.Point(280, 184), pya.Point(-100, 184)])
nselect = pya.Polygon([pya.Point(-320, -120), pya.Point(520, -120), pya.Point(520, 320), pya.Point(-320, 320)])

top_cell.shapes(gate_layer).insert(gate)
top_cell.shapes(active_layer).insert(active)
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon20.gds")
