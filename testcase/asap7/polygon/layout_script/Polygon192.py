import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon192")


active_layer = layout.layer(11, 0)
pselect_layer = layout.layer(13, 0)

pselect = pya.Polygon([pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 800), pya.Point(0, 800)])
top_cell.shapes(pselect_layer).insert(pselect)

active = pya.Polygon([pya.Point(120, 292), pya.Point(280, 292), pya.Point(280, 508), pya.Point(120, 508)])
top_cell.shapes(active_layer).insert(active)

layout.write("../gds/Polygon192.gds")
