import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon194")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
lisd_layer = layout.layer(17, 0)
sdt_layer = layout.layer(88, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(320, 0), pya.Point(320, 216), pya.Point(0, 216)])
top_cell.shapes(active_layer).insert(active)

lisd = pya.Polygon([pya.Point(0, 0), pya.Point(320, 0), pya.Point(320, 216), pya.Point(0, 216)])
top_cell.shapes(lisd_layer).insert(lisd)

sdt = pya.Polygon([pya.Point(40, 40), pya.Point(200, 40), pya.Point(200, 160), pya.Point(40, 160)])
top_cell.shapes(sdt_layer).insert(sdt)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(520, -120), pya.Point(520, 336), pya.Point(-200, 336)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon194.gds")
