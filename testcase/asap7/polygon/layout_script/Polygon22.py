import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon22")


gate_layer = layout.layer(7, 0)
active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)

gate1 = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 216), pya.Point(0, 216)])
gate2 = pya.Polygon([pya.Point(308, 0), pya.Point(388, 0), pya.Point(388, 216), pya.Point(308, 216)])
active = pya.Polygon([pya.Point(-100, 16), pya.Point(280, 16), pya.Point(280, 200), pya.Point(-100, 200)])
nselect = pya.Polygon([pya.Point(-320, -120), pya.Point(600, -120), pya.Point(600, 320), pya.Point(-320, 320)])

top_cell.shapes(gate_layer).insert(gate1)
top_cell.shapes(gate_layer).insert(gate2)
top_cell.shapes(active_layer).insert(active)
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon22.gds")
