import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon6")


well_layer = layout.layer(1, 0)
active_layer = layout.layer(11, 0)
gate_layer = layout.layer(7, 0)
pselect_layer = layout.layer(13, 0)

well = pya.Polygon([pya.Point(-800, -800), pya.Point(1600, -800), pya.Point(1600, 1600), pya.Point(-800, 1600)])
top_cell.shapes(well_layer).insert(well)

active = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 240), pya.Point(0, 240)])
top_cell.shapes(active_layer).insert(active)

gate = pya.Polygon([pya.Point(200, -40), pya.Point(280, -40), pya.Point(280, 280), pya.Point(200, 280)])
top_cell.shapes(gate_layer).insert(gate)

pselect = pya.Polygon([pya.Point(-400, -400), pya.Point(1200, -400), pya.Point(1200, 800), pya.Point(-400, 800)])
top_cell.shapes(pselect_layer).insert(pselect)


layout.write("../gds/Polygon6.gds")
