import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon200")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
lisd_layer = layout.layer(17, 0)
sdt_layer = layout.layer(88, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 108), pya.Point(0, 108)])
top_cell.shapes(active_layer).insert(active)

sdt = pya.Polygon([pya.Point(40, 0), pya.Point(400, 0), pya.Point(400, 108), pya.Point(40, 108)])
top_cell.shapes(sdt_layer).insert(sdt)

lisd = pya.Polygon([pya.Point(20, 40), pya.Point(800, 40), pya.Point(800, 148), pya.Point(20, 148)])
top_cell.shapes(lisd_layer).insert(lisd)

nselect = pya.Polygon([pya.Point(-400, -400), pya.Point(1600, -400), pya.Point(1600, 800), pya.Point(-400, 800)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon200.gds")
