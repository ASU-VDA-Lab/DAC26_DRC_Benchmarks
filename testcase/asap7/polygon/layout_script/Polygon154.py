import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon154")


m8_layer = layout.layer(80, 0)

m8_1 = pya.Polygon([pya.Point(0, 0), pya.Point(160, 0), pya.Point(160, 752), pya.Point(0, 752)])
top_cell.shapes(m8_layer).insert(m8_1)

m8_2 = pya.Polygon([pya.Point(-296, 912), pya.Point(456, 912), pya.Point(456, 1072), pya.Point(-296, 1072)])
top_cell.shapes(m8_layer).insert(m8_2)

layout.write("../gds/Polygon154.gds")
