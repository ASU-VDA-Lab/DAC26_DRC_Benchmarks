import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon33")


gate_layer = layout.layer(7, 0)
gcut_layer = layout.layer(10, 0)
active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)

gate = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 216), pya.Point(0, 216)])
gcut = pya.Polygon([pya.Point(-80, 100), pya.Point(160, 100), pya.Point(160, 168), pya.Point(-80, 168)])
active = pya.Polygon([pya.Point(-100, 60), pya.Point(280, 60), pya.Point(280, 180), pya.Point(-100, 180)])
nselect = pya.Polygon([pya.Point(-320, -120), pya.Point(520, -120), pya.Point(520, 320), pya.Point(-320, 320)])

top_cell.shapes(gate_layer).insert(gate)
top_cell.shapes(gcut_layer).insert(gcut)
top_cell.shapes(active_layer).insert(active)
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon33.gds")
