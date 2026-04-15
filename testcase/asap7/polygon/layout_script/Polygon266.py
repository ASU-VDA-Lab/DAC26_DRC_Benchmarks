import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon266")

v2_layer = layout.layer(25, 0)
m2_layer = layout.layer(20, 0)
m3_layer = layout.layer(30, 0)


top_cell.shapes(v2_layer).insert(pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)]))
top_cell.shapes(m3_layer).insert(pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)]))
top_cell.shapes(v2_layer).insert(pya.Polygon([pya.Point(40, 148), pya.Point(112, 148), pya.Point(112, 220), pya.Point(40, 220)]))
top_cell.shapes(m3_layer).insert(pya.Polygon([pya.Point(40, 148), pya.Point(112, 148), pya.Point(112, 220), pya.Point(40, 220)]))

top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(-20, -20), pya.Point(132, -20), pya.Point(132, 240), pya.Point(-20, 240)]))


top_cell.shapes(v2_layer).insert(pya.Polygon([pya.Point(0, 800), pya.Point(72, 800), pya.Point(72, 872), pya.Point(0, 872)]))
top_cell.shapes(m3_layer).insert(pya.Polygon([pya.Point(0, 800), pya.Point(72, 800), pya.Point(72, 872), pya.Point(0, 872)]))
top_cell.shapes(v2_layer).insert(pya.Polygon([pya.Point(140, 800), pya.Point(212, 800), pya.Point(212, 872), pya.Point(140, 872)]))
top_cell.shapes(m3_layer).insert(pya.Polygon([pya.Point(140, 800), pya.Point(212, 800), pya.Point(212, 872), pya.Point(140, 872)]))

top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(-20, 780), pya.Point(232, 780), pya.Point(232, 892), pya.Point(-20, 892)]))


top_cell.shapes(v2_layer).insert(pya.Polygon([pya.Point(0, 1600), pya.Point(72, 1600), pya.Point(72, 1672), pya.Point(0, 1672)]))
top_cell.shapes(m3_layer).insert(pya.Polygon([pya.Point(0, 1600), pya.Point(72, 1600), pya.Point(72, 1672), pya.Point(0, 1672)]))
top_cell.shapes(v2_layer).insert(pya.Polygon([pya.Point(113, 1601), pya.Point(185, 1601), pya.Point(185, 1673), pya.Point(113, 1673)]))
top_cell.shapes(m3_layer).insert(pya.Polygon([pya.Point(113, 1601), pya.Point(185, 1601), pya.Point(185, 1673), pya.Point(113, 1673)]))

top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(-20, 1580), pya.Point(208, 1580), pya.Point(208, 1692), pya.Point(-20, 1692)]))

layout.write("../gds/Polygon266.gds")
