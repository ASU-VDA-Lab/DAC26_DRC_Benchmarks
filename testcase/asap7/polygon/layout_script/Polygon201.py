import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon201")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
lisd_layer = layout.layer(17, 0)
sdt_layer = layout.layer(88, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(360, 0), pya.Point(360, 108), pya.Point(0, 108)])
top_cell.shapes(active_layer).insert(active)

lisd = pya.Polygon([pya.Point(0, 0), pya.Point(360, 0), pya.Point(360, 108), pya.Point(0, 108)])
top_cell.shapes(lisd_layer).insert(lisd)

sdt1 = pya.Polygon([pya.Point(40, 0), pya.Point(136, 0), pya.Point(136, 108), pya.Point(40, 108)])
top_cell.shapes(sdt_layer).insert(sdt1)

sdt2 = pya.Polygon([pya.Point(224, 0), pya.Point(320, 0), pya.Point(320, 108), pya.Point(224, 108)])
top_cell.shapes(sdt_layer).insert(sdt2)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(560, -120), pya.Point(560, 228), pya.Point(-200, 228)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon201.gds")
