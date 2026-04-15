import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon235")


active_layer = layout.layer(11, 0)
sramvt_layer = layout.layer(110, 0)
nselect_layer = layout.layer(12, 0)

active = pya.Polygon([pya.Point(184, 80), pya.Point(344, 80), pya.Point(344, 188), pya.Point(184, 188)])
top_cell.shapes(active_layer).insert(active)

sramvt = pya.Polygon([pya.Point(0, 0), pya.Point(528, 0), pya.Point(528, 268), pya.Point(0, 268)])
top_cell.shapes(sramvt_layer).insert(sramvt)

nselect = pya.Polygon([pya.Point(-16, -40), pya.Point(544, -40), pya.Point(544, 308), pya.Point(-16, 308)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon235.gds")
