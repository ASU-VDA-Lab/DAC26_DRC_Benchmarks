import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon248")

v0_layer = layout.layer(18, 0)
m1_layer = layout.layer(19, 0)
lisd_layer = layout.layer(17, 0)


top_cell.shapes(v0_layer).insert(pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)]))
top_cell.shapes(m1_layer).insert(pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)]))
top_cell.shapes(v0_layer).insert(pya.Polygon([pya.Point(40, 148), pya.Point(112, 148), pya.Point(112, 220), pya.Point(40, 220)]))
top_cell.shapes(m1_layer).insert(pya.Polygon([pya.Point(40, 148), pya.Point(112, 148), pya.Point(112, 220), pya.Point(40, 220)]))


top_cell.shapes(v0_layer).insert(pya.Polygon([pya.Point(0, 800), pya.Point(72, 800), pya.Point(72, 872), pya.Point(0, 872)]))
top_cell.shapes(m1_layer).insert(pya.Polygon([pya.Point(0, 800), pya.Point(72, 800), pya.Point(72, 872), pya.Point(0, 872)]))
top_cell.shapes(v0_layer).insert(pya.Polygon([pya.Point(140, 800), pya.Point(212, 800), pya.Point(212, 872), pya.Point(140, 872)]))
top_cell.shapes(m1_layer).insert(pya.Polygon([pya.Point(140, 800), pya.Point(212, 800), pya.Point(212, 872), pya.Point(140, 872)]))


top_cell.shapes(v0_layer).insert(pya.Polygon([pya.Point(0, 1600), pya.Point(72, 1600), pya.Point(72, 1672), pya.Point(0, 1672)]))
top_cell.shapes(m1_layer).insert(pya.Polygon([pya.Point(0, 1600), pya.Point(72, 1600), pya.Point(72, 1672), pya.Point(0, 1672)]))
top_cell.shapes(v0_layer).insert(pya.Polygon([pya.Point(113, 1601), pya.Point(185, 1601), pya.Point(185, 1673), pya.Point(113, 1673)]))
top_cell.shapes(m1_layer).insert(pya.Polygon([pya.Point(113, 1601), pya.Point(185, 1601), pya.Point(185, 1673), pya.Point(113, 1673)]))

lisd = pya.Polygon([pya.Point(-40, -40), pya.Point(260, -40), pya.Point(260, 1720), pya.Point(-40, 1720)])
top_cell.shapes(lisd_layer).insert(lisd)

layout.write("../gds/Polygon248.gds")
