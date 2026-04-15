import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon88")


m3_layer = layout.layer(30, 0)

m3_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 200), pya.Point(0, 200)])
top_cell.shapes(m3_layer).insert(m3_1)

m3_2 = pya.Polygon([pya.Point(128, 0), pya.Point(200, 0), pya.Point(200, 200), pya.Point(128, 200)])
top_cell.shapes(m3_layer).insert(m3_2)

layout.write("../gds/Polygon88.gds")
