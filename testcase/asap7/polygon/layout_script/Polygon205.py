import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon205")


active_layer = layout.layer(11, 0)
slvt_layer = layout.layer(97, 0)
nselect_layer = layout.layer(12, 0)

active = pya.Polygon([pya.Point(160, 108), pya.Point(320, 108), pya.Point(320, 216), pya.Point(160, 216)])
top_cell.shapes(active_layer).insert(active)

slvt = pya.Polygon([pya.Point(0, 0), pya.Point(440, 0), pya.Point(440, 324), pya.Point(0, 324)])
top_cell.shapes(slvt_layer).insert(slvt)

nselect = pya.Polygon([pya.Point(-40, -12), pya.Point(520, -12), pya.Point(520, 336), pya.Point(-40, 336)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon205.gds")
