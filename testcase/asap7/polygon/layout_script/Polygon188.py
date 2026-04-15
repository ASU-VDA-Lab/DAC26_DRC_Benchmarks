import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon188")


active_layer = layout.layer(11, 0)
pselect_layer = layout.layer(13, 0)

active = pya.Polygon([pya.Point(160, 108), pya.Point(320, 108), pya.Point(320, 216), pya.Point(160, 216)])
top_cell.shapes(active_layer).insert(active)

pselect = pya.Polygon([pya.Point(0, 0), pya.Point(440, 0), pya.Point(440, 324), pya.Point(0, 324)])
top_cell.shapes(pselect_layer).insert(pselect)

layout.write("../gds/Polygon188.gds")
