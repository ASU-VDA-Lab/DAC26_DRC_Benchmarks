import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon3")


active_layer = layout.layer(11, 0)
pselect_layer = layout.layer(13, 0)

pselect = pya.Polygon([pya.Point(160, 0), pya.Point(800, 0), pya.Point(800, 1040), pya.Point(160, 1040)])
top_cell.shapes(pselect_layer).insert(pselect)

top_active = pya.Polygon([pya.Point(240, 728), pya.Point(720, 728), pya.Point(720, 944), pya.Point(240, 944)])
top_cell.shapes(active_layer).insert(top_active)

mid_active = pya.Polygon([pya.Point(240, 404), pya.Point(800, 404), pya.Point(800, 620), pya.Point(240, 620)])
top_cell.shapes(active_layer).insert(mid_active)

bot_active = pya.Polygon([pya.Point(40, 80), pya.Point(680, 80), pya.Point(680, 296), pya.Point(40, 296)])
top_cell.shapes(active_layer).insert(bot_active)

layout.write("../gds/Polygon3.gds")
