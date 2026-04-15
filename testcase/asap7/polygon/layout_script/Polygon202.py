import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon202")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
lisd_layer = layout.layer(17, 0)
sdt_layer = layout.layer(88, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(320, 0), pya.Point(320, 108), pya.Point(0, 108)])
top_cell.shapes(active_layer).insert(active)

lisd = pya.Polygon([pya.Point(0, 0), pya.Point(320, 0), pya.Point(320, 108), pya.Point(0, 108)])
top_cell.shapes(lisd_layer).insert(lisd)

sdt = pya.Polygon([pya.Point(40, 0), pya.Point(120, 0), pya.Point(120, 108), pya.Point(40, 108)])
top_cell.shapes(sdt_layer).insert(sdt)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(520, -120), pya.Point(520, 228), pya.Point(-200, 228)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon202.gds")
