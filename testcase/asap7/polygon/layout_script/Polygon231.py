import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon231")


active_layer = layout.layer(11, 0)
slvt_layer = layout.layer(97, 0)
nselect_layer = layout.layer(12, 0)
sramdrc_layer = layout.layer(99, 0)

active = pya.Polygon([pya.Point(80, 40), pya.Point(240, 40), pya.Point(240, 148), pya.Point(80, 148)])
top_cell.shapes(active_layer).insert(active)

sramdrc = pya.Polygon([pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 240), pya.Point(0, 240)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

slvt = pya.Polygon([pya.Point(0, 0), pya.Point(320, 0), pya.Point(320, 188), pya.Point(0, 188)])
top_cell.shapes(slvt_layer).insert(slvt)

nselect = pya.Polygon([pya.Point(-120, -80), pya.Point(360, -80), pya.Point(360, 228), pya.Point(-120, 228)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon231.gds")
