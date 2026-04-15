import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon93")


m3_layer = layout.layer(30, 0)

m3_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 120), pya.Point(0, 120)])
top_cell.shapes(m3_layer).insert(m3_1)

m3_2 = pya.Polygon([pya.Point(128, 140), pya.Point(200, 140), pya.Point(200, 260), pya.Point(128, 260)])
top_cell.shapes(m3_layer).insert(m3_2)

layout.write("../gds/Polygon93.gds")
