import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon197")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
lisd_layer = layout.layer(17, 0)
sdt_layer = layout.layer(88, 0)
gate_layer = layout.layer(7, 0)

gate = pya.Polygon([pya.Point(80, 0), pya.Point(160, 0), pya.Point(160, 216), pya.Point(80, 216)])
top_cell.shapes(gate_layer).insert(gate)

active = pya.Polygon([pya.Point(-100, 16), pya.Point(100, 16), pya.Point(100, 200), pya.Point(-100, 200)])
top_cell.shapes(active_layer).insert(active)

lisd = pya.Polygon([pya.Point(-100, 16), pya.Point(100, 16), pya.Point(100, 200), pya.Point(-100, 200)])
top_cell.shapes(lisd_layer).insert(lisd)

sdt = pya.Polygon([pya.Point(20, 16), pya.Point(120, 16), pya.Point(120, 200), pya.Point(20, 200)])
top_cell.shapes(sdt_layer).insert(sdt)

nselect = pya.Polygon([pya.Point(-320, -120), pya.Point(520, -120), pya.Point(520, 320), pya.Point(-320, 320)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon197.gds")
