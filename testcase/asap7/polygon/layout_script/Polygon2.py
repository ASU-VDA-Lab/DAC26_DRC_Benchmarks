import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon2")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)


active = pya.Polygon([ pya.Point(0, 0), pya.Point(2000, 0), pya.Point(2000, 2000), pya.Point(0, 2000), ])
active.insert_hole([ pya.Point(400, 400), pya.Point(400, 508), pya.Point(508, 508), pya.Point(508, 400), ])
top_cell.shapes(active_layer).insert(active)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(2200, -120), pya.Point(2200, 2120), pya.Point(-200, 2120)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon2.gds")
