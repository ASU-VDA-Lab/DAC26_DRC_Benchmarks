import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon13")


active_layer = layout.layer(11, 0)
well_layer = layout.layer(1, 0)
pselect_layer = layout.layer(13, 0)

well = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(0, 800)])
top_cell.shapes(well_layer).insert(well)

active = pya.Polygon([pya.Point(200, 40), pya.Point(600, 40), pya.Point(600, 256), pya.Point(200, 256)])
top_cell.shapes(active_layer).insert(active)

pselect = pya.Polygon([pya.Point(-120, -80), pya.Point(920, -80), pya.Point(920, 376), pya.Point(-120, 376)])
top_cell.shapes(pselect_layer).insert(pselect)

layout.write("../gds/Polygon13.gds")
