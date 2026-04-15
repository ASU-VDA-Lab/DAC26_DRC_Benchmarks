import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon14")


active_layer = layout.layer(11, 0)
well_layer = layout.layer(1, 0)
nselect_layer = layout.layer(12, 0)

well = pya.Polygon([pya.Point(0, 296), pya.Point(800, 296), pya.Point(800, 1096), pya.Point(0, 1096)])
top_cell.shapes(well_layer).insert(well)

active = pya.Polygon([pya.Point(120, 0), pya.Point(520, 0), pya.Point(520, 216), pya.Point(120, 216)])
top_cell.shapes(active_layer).insert(active)

nselect = pya.Polygon([pya.Point(-80, -120), pya.Point(720, -120), pya.Point(720, 336), pya.Point(-80, 336)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon14.gds")
