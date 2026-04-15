import pya

layout = pya.Layout()
layout.dbu = 0.00025


top_cell = layout.create_cell("Polygon69")

m1_layer = layout.layer(19, 0)
v0_layer = layout.layer(18, 0)
lisd_layer = layout.layer(17, 0)


m1_rect1 = pya.Polygon([pya.Point(800, 6400), pya.Point(872, 6400), pya.Point(872, 8400), pya.Point(800, 8400)])
top_cell.shapes(m1_layer).insert(m1_rect1)

m1_rect2 = pya.Polygon([pya.Point(7200, 800), pya.Point(10000, 800), pya.Point(10000, 872), pya.Point(7200, 872)])
top_cell.shapes(m1_layer).insert(m1_rect2)

m1_rect3 = pya.Polygon([pya.Point(4800, 15200), pya.Point(8800, 15200), pya.Point(8800, 15272), pya.Point(4800, 15272)])
top_cell.shapes(m1_layer).insert(m1_rect3)

m1_rect4 = pya.Polygon([pya.Point(15200, 6400), pya.Point(15272, 6400), pya.Point(15272, 10800), pya.Point(15200, 10800)])
top_cell.shapes(m1_layer).insert(m1_rect4)

m1_rect5 = pya.Polygon([pya.Point(14200, 6400), pya.Point(14272, 6400), pya.Point(14272, 6800), pya.Point(14200, 6800)])
top_cell.shapes(m1_layer).insert(m1_rect5)

v0_rect = pya.Polygon([pya.Point(14200, 6520), pya.Point(14272, 6520), pya.Point(14272, 6592), pya.Point(14200, 6592)])
top_cell.shapes(v0_layer).insert(v0_rect)

lisd_rect = pya.Polygon([pya.Point(12588, 6508), pya.Point(18612, 6508), pya.Point(18612, 6604), pya.Point(12588, 6604)])
top_cell.shapes(lisd_layer).insert(lisd_rect)

layout.write("../gds/Polygon69.gds")
