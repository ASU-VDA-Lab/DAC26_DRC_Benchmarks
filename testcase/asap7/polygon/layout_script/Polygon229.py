import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon229")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
lisd_layer = layout.layer(17, 0)
sdt_layer = layout.layer(88, 0)
sramdrc_layer = layout.layer(99, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(320, 0), pya.Point(320, 56), pya.Point(0, 56)])
top_cell.shapes(active_layer).insert(active)

lisd = pya.Polygon([pya.Point(0, 0), pya.Point(320, 0), pya.Point(320, 56), pya.Point(0, 56)])
top_cell.shapes(lisd_layer).insert(lisd)

sdt = pya.Polygon([pya.Point(40, 0), pya.Point(200, 0), pya.Point(200, 56), pya.Point(40, 56)])
top_cell.shapes(sdt_layer).insert(sdt)

sramdrc = pya.Polygon([pya.Point(-40, -40), pya.Point(360, -40), pya.Point(360, 96), pya.Point(-40, 96)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(520, -120), pya.Point(520, 176), pya.Point(-200, 176)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon229.gds")
