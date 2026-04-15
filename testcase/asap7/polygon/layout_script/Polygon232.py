import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon232")


active_layer = layout.layer(11, 0)
sramvt_layer = layout.layer(110, 0)
nselect_layer = layout.layer(12, 0)
sramdrc_layer = layout.layer(99, 0)

active = pya.Polygon([pya.Point(40, 60), pya.Point(200, 60), pya.Point(200, 168), pya.Point(40, 168)])
top_cell.shapes(active_layer).insert(active)

sramdrc = pya.Polygon([pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 240), pya.Point(0, 240)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

sramvt = pya.Polygon([pya.Point(0, 0), pya.Point(240, 0), pya.Point(240, 240), pya.Point(0, 240)])
top_cell.shapes(sramvt_layer).insert(sramvt)

nselect = pya.Polygon([pya.Point(-160, -60), pya.Point(360, -60), pya.Point(360, 228), pya.Point(-160, 228)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon232.gds")
