import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon238")


active_layer = layout.layer(11, 0)
sramvt_layer = layout.layer(110, 0)
nselect_layer = layout.layer(12, 0)

sramvt = pya.Polygon([pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 800), pya.Point(0, 800)])
top_cell.shapes(sramvt_layer).insert(sramvt)

active = pya.Polygon([pya.Point(120, 292), pya.Point(280, 292), pya.Point(280, 508), pya.Point(120, 508)])
top_cell.shapes(active_layer).insert(active)

nselect = pya.Polygon([pya.Point(-80, 172), pya.Point(480, 172), pya.Point(480, 628), pya.Point(-80, 628)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon238.gds")
