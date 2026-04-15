import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon8")


active_layer = layout.layer(11, 0)
gate_layer = layout.layer(7, 0)
nselect_layer = layout.layer(12, 0)

gate1 = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 216), pya.Point(0, 216)])
top_cell.shapes(gate_layer).insert(gate1)

gate2 = pya.Polygon([pya.Point(440, 0), pya.Point(520, 0), pya.Point(520, 216), pya.Point(440, 216)])
top_cell.shapes(gate_layer).insert(gate2)

active1 = pya.Polygon([pya.Point(-100, 16), pya.Point(160, 16), pya.Point(160, 200), pya.Point(-100, 200)])
top_cell.shapes(active_layer).insert(active1)

active2 = pya.Polygon([pya.Point(260, 16), pya.Point(640, 16), pya.Point(640, 200), pya.Point(260, 200)])
top_cell.shapes(active_layer).insert(active2)

nselect = pya.Polygon([pya.Point(-320, -120), pya.Point(880, -120), pya.Point(880, 320), pya.Point(-320, 320)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon8.gds")
