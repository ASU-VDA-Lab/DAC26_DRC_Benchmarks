import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon275")

v3_layer = layout.layer(35, 0)
m3_layer = layout.layer(30, 0)
m4_layer = layout.layer(40, 0)


top_cell.shapes(v3_layer).insert(pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)]))
top_cell.shapes(m4_layer).insert(pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)]))
top_cell.shapes(v3_layer).insert(pya.Polygon([pya.Point(148, 40), pya.Point(220, 40), pya.Point(220, 112), pya.Point(148, 112)]))
top_cell.shapes(m4_layer).insert(pya.Polygon([pya.Point(148, 40), pya.Point(220, 40), pya.Point(220, 112), pya.Point(148, 112)]))

top_cell.shapes(m3_layer).insert(pya.Polygon([pya.Point(-20, -20), pya.Point(240, -20), pya.Point(240, 132), pya.Point(-20, 132)]))


top_cell.shapes(v3_layer).insert(pya.Polygon([pya.Point(0, 800), pya.Point(72, 800), pya.Point(72, 872), pya.Point(0, 872)]))
top_cell.shapes(m4_layer).insert(pya.Polygon([pya.Point(0, 800), pya.Point(72, 800), pya.Point(72, 872), pya.Point(0, 872)]))
top_cell.shapes(v3_layer).insert(pya.Polygon([pya.Point(0, 940), pya.Point(72, 940), pya.Point(72, 1012), pya.Point(0, 1012)]))
top_cell.shapes(m4_layer).insert(pya.Polygon([pya.Point(0, 940), pya.Point(72, 940), pya.Point(72, 1012), pya.Point(0, 1012)]))

top_cell.shapes(m3_layer).insert(pya.Polygon([pya.Point(-20, 780), pya.Point(92, 780), pya.Point(92, 1032), pya.Point(-20, 1032)]))


top_cell.shapes(v3_layer).insert(pya.Polygon([pya.Point(0, 1600), pya.Point(72, 1600), pya.Point(72, 1672), pya.Point(0, 1672)]))
top_cell.shapes(m4_layer).insert(pya.Polygon([pya.Point(0, 1600), pya.Point(72, 1600), pya.Point(72, 1672), pya.Point(0, 1672)]))
top_cell.shapes(v3_layer).insert(pya.Polygon([pya.Point(113, 1601), pya.Point(185, 1601), pya.Point(185, 1673), pya.Point(113, 1673)]))
top_cell.shapes(m4_layer).insert(pya.Polygon([pya.Point(113, 1601), pya.Point(185, 1601), pya.Point(185, 1673), pya.Point(113, 1673)]))

top_cell.shapes(m3_layer).insert(pya.Polygon([pya.Point(-20, 1580), pya.Point(208, 1580), pya.Point(208, 1692), pya.Point(-20, 1692)]))

layout.write("../gds/Polygon275.gds")
