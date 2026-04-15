import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon64")


active_layer = layout.layer(11, 0)
gate_layer = layout.layer(7, 0)
lvt_layer = layout.layer(98, 0)
nselect_layer = layout.layer(12, 0)

gate = pya.Polygon([pya.Point(200, 0), pya.Point(280, 0), pya.Point(280, 216), pya.Point(200, 216)])
top_cell.shapes(gate_layer).insert(gate)

active = pya.Polygon([pya.Point(80, 16), pya.Point(520, 16), pya.Point(520, 200), pya.Point(80, 200)])
top_cell.shapes(active_layer).insert(active)

lvt = pya.Polygon([pya.Point(180, -40), pya.Point(800, -40), pya.Point(800, 256), pya.Point(180, 256)])
top_cell.shapes(lvt_layer).insert(lvt)

nselect = pya.Polygon([pya.Point(-120, -120), pya.Point(720, -120), pya.Point(720, 320), pya.Point(-120, 320)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon64.gds")
