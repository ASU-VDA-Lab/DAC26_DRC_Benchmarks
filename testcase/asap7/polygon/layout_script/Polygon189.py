import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon189")


active_layer = layout.layer(11, 0)
pselect_layer = layout.layer(13, 0)

active = pya.Polygon([pya.Point(184, 80), pya.Point(344, 80), pya.Point(344, 188), pya.Point(184, 188)])
top_cell.shapes(active_layer).insert(active)

pselect = pya.Polygon([pya.Point(0, 0), pya.Point(528, 0), pya.Point(528, 268), pya.Point(0, 268)])
top_cell.shapes(pselect_layer).insert(pselect)

layout.write("../gds/Polygon189.gds")
