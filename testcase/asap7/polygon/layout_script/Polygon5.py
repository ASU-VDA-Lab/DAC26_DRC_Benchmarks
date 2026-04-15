import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon5")


active_layer = layout.layer(11, 0)
fin_layer = layout.layer(2, 0)
nselect_layer = layout.layer(12, 0)

fin = pya.Polygon([pya.Point(0, 160), pya.Point(800, 160), pya.Point(800, 188), pya.Point(0, 188)])
top_cell.shapes(fin_layer).insert(fin)

active = pya.Polygon([pya.Point(292, 132), pya.Point(508, 132), pya.Point(508, 240), pya.Point(292, 240)])
top_cell.shapes(active_layer).insert(active)

nselect = pya.Polygon([pya.Point(-120, -40), pya.Point(920, -40), pya.Point(920, 360), pya.Point(-120, 360)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon5.gds")
