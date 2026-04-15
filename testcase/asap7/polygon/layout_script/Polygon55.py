import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon55")


lig_layer = layout.layer(16, 0)
active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
lisd_layer = layout.layer(17, 0)
sdt_layer = layout.layer(88, 0)

lig = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 200), pya.Point(0, 200)])
top_cell.shapes(lig_layer).insert(lig)

sdt = pya.Polygon([pya.Point(120, 16), pya.Point(240, 16), pya.Point(240, 200), pya.Point(120, 200)])
top_cell.shapes(sdt_layer).insert(sdt)

active = pya.Polygon([pya.Point(100, -40), pya.Point(260, -40), pya.Point(260, 240), pya.Point(100, 240)])
top_cell.shapes(active_layer).insert(active)

lisd = pya.Polygon([pya.Point(100, -40), pya.Point(260, -40), pya.Point(260, 240), pya.Point(100, 240)])
top_cell.shapes(lisd_layer).insert(lisd)

nselect = pya.Polygon([pya.Point(-120, -160), pya.Point(480, -160), pya.Point(480, 360), pya.Point(-120, 360)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon55.gds")
