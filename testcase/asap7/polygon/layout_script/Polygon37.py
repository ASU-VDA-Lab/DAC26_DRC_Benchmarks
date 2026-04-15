import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon37")


gate_layer = layout.layer(7, 0)
gcut_layer = layout.layer(10, 0)

gate = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 216), pya.Point(0, 216)])
gcut = pya.Polygon([pya.Point(-80, 80), pya.Point(160, 80), pya.Point(160, 140), pya.Point(-80, 140)])

top_cell.shapes(gate_layer).insert(gate)
top_cell.shapes(gcut_layer).insert(gcut)

layout.write("../gds/Polygon37.gds")
