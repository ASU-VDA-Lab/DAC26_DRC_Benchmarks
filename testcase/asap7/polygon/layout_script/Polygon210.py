import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon210")


active_layer = layout.layer(11, 0)
slvt_layer = layout.layer(97, 0)
nselect_layer = layout.layer(12, 0)

slvt = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 200), pya.Point(0, 200)])
top_cell.shapes(slvt_layer).insert(slvt)

active = pya.Polygon([pya.Point(320, 44), pya.Point(480, 44), pya.Point(480, 152), pya.Point(320, 152)])
top_cell.shapes(active_layer).insert(active)

nselect = pya.Polygon([pya.Point(120, -76), pya.Point(680, -76), pya.Point(680, 272), pya.Point(120, 272)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon210.gds")
