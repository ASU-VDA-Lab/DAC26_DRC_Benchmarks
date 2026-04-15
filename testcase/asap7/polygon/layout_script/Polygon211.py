import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon211")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
sramdrc_layer = layout.layer(99, 0)

active = pya.Polygon([pya.Point(0, 0), pya.Point(60, 0), pya.Point(60, 108), pya.Point(0, 108)])
top_cell.shapes(active_layer).insert(active)

sramdrc = pya.Polygon([pya.Point(-40, -40), pya.Point(100, -40), pya.Point(100, 148), pya.Point(-40, 148)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(260, -120), pya.Point(260, 228), pya.Point(-200, 228)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon211.gds")
