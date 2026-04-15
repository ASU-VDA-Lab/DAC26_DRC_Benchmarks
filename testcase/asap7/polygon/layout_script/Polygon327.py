import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon327")


nwell_layer = layout.layer(1, 0)
gate_layer = layout.layer(7, 0)

nwell = pya.Polygon([pya.Point(0, 0), pya.Point(600, 0), pya.Point(600, 800), pya.Point(0, 800)])
gate = pya.Polygon([pya.Point(20, 200), pya.Point(100, 200), pya.Point(100, 416), pya.Point(20, 416)])

top_cell.shapes(nwell_layer).insert(nwell)
top_cell.shapes(gate_layer).insert(gate)

layout.write("../gds/Polygon327.gds")
