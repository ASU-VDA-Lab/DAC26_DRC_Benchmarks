import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon35")


gate_layer = layout.layer(7, 0)
gcut_layer = layout.layer(10, 0)

gate1 = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 216), pya.Point(0, 216)])
gate2 = pya.Polygon([pya.Point(216, 0), pya.Point(296, 0), pya.Point(296, 216), pya.Point(216, 216)])
gcut = pya.Polygon([pya.Point(-80, 80), pya.Point(160, 80), pya.Point(160, 148), pya.Point(-80, 148)])

top_cell.shapes(gate_layer).insert(gate1)
top_cell.shapes(gate_layer).insert(gate2)
top_cell.shapes(gcut_layer).insert(gcut)

layout.write("../gds/Polygon35.gds")
