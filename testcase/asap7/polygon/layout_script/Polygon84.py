import pya

layout = pya.Layout()
layout.dbu = 0.00025


top_cell = layout.create_cell("Polygon84")

m2_layer = layout.layer(20, 0)


bottom_left = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 240), pya.Point(0, 240)])
top_cell.shapes(m2_layer).insert(bottom_left)

bottom_right = pya.Polygon([pya.Point(872, 0), pya.Point(1672, 0), pya.Point(1672, 240), pya.Point(872, 240)])
top_cell.shapes(m2_layer).insert(bottom_right)

top_left = pya.Polygon([pya.Point(760, 320), pya.Point(1560, 320), pya.Point(1560, 560), pya.Point(760, 560)])
top_cell.shapes(m2_layer).insert(top_left)

top_right = pya.Polygon([pya.Point(1632, 320), pya.Point(2432, 320), pya.Point(2432, 560), pya.Point(1632, 560)])
top_cell.shapes(m2_layer).insert(top_right)

layout.write("../gds/Polygon84.gds")
