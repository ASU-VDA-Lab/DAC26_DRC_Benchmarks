import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon169")


m9_layer = layout.layer(90, 0)

m9_1 = pya.Polygon([pya.Point(0, 0), pya.Point(160, 0), pya.Point(160, 752), pya.Point(0, 752)])
top_cell.shapes(m9_layer).insert(m9_1)

m9_2 = pya.Polygon([pya.Point(-296, 912), pya.Point(456, 912), pya.Point(456, 1072), pya.Point(-296, 1072)])
top_cell.shapes(m9_layer).insert(m9_2)

layout.write("../gds/Polygon169.gds")
