import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon257")

v1_layer = layout.layer(21, 0)
m1_layer = layout.layer(19, 0)
m2_layer = layout.layer(20, 0)


top_cell.shapes(v1_layer).insert(pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)]))
top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)]))
top_cell.shapes(v1_layer).insert(pya.Polygon([pya.Point(148, 40), pya.Point(220, 40), pya.Point(220, 112), pya.Point(148, 112)]))
top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(148, 40), pya.Point(220, 40), pya.Point(220, 112), pya.Point(148, 112)]))

top_cell.shapes(m1_layer).insert(pya.Polygon([pya.Point(-20, -8), pya.Point(240, -8), pya.Point(240, 128), pya.Point(-20, 128)]))


top_cell.shapes(v1_layer).insert(pya.Polygon([pya.Point(0, 800), pya.Point(72, 800), pya.Point(72, 872), pya.Point(0, 872)]))
top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(0, 800), pya.Point(72, 800), pya.Point(72, 872), pya.Point(0, 872)]))
top_cell.shapes(v1_layer).insert(pya.Polygon([pya.Point(0, 940), pya.Point(72, 940), pya.Point(72, 1012), pya.Point(0, 1012)]))
top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(0, 940), pya.Point(72, 940), pya.Point(72, 1012), pya.Point(0, 1012)]))

top_cell.shapes(m1_layer).insert(pya.Polygon([pya.Point(-20, 792), pya.Point(92, 792), pya.Point(92, 1020), pya.Point(-20, 1020)]))


top_cell.shapes(v1_layer).insert(pya.Polygon([pya.Point(0, 1600), pya.Point(72, 1600), pya.Point(72, 1672), pya.Point(0, 1672)]))
top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(0, 1600), pya.Point(72, 1600), pya.Point(72, 1672), pya.Point(0, 1672)]))
top_cell.shapes(v1_layer).insert(pya.Polygon([pya.Point(113, 1601), pya.Point(185, 1601), pya.Point(185, 1673), pya.Point(113, 1673)]))
top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(113, 1601), pya.Point(185, 1601), pya.Point(185, 1673), pya.Point(113, 1673)]))

top_cell.shapes(m1_layer).insert(pya.Polygon([pya.Point(-20, 1592), pya.Point(208, 1592), pya.Point(208, 1680), pya.Point(-20, 1680)]))

layout.write("../gds/Polygon257.gds")
