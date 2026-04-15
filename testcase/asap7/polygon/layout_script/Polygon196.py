import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon196")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
lisd_layer = layout.layer(17, 0)
sdt_layer = layout.layer(88, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(320, 0), pya.Point(320, 108), pya.Point(0, 108)])
top_cell.shapes(active_layer).insert(active)

sdt = pya.Polygon([pya.Point(40, -40), pya.Point(200, -40), pya.Point(200, 68), pya.Point(40, 68)])
top_cell.shapes(sdt_layer).insert(sdt)

lisd = pya.Polygon([pya.Point(40, -40), pya.Point(200, -40), pya.Point(200, 68), pya.Point(40, 68)])
top_cell.shapes(lisd_layer).insert(lisd)

nselect = pya.Polygon([pya.Point(-200, -160), pya.Point(520, -160), pya.Point(520, 228), pya.Point(-200, 228)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon196.gds")
