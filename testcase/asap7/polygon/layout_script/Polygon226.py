import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon226")


active_layer = layout.layer(11, 0)
pselect_layer = layout.layer(13, 0)
sramdrc_layer = layout.layer(99, 0)

active = pya.Polygon([pya.Point(80, 40), pya.Point(240, 40), pya.Point(240, 148), pya.Point(80, 148)])
top_cell.shapes(active_layer).insert(active)

sramdrc = pya.Polygon([pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 240), pya.Point(0, 240)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

pselect = pya.Polygon([pya.Point(0, 0), pya.Point(320, 0), pya.Point(320, 188), pya.Point(0, 188)])
top_cell.shapes(pselect_layer).insert(pselect)

layout.write("../gds/Polygon226.gds")
