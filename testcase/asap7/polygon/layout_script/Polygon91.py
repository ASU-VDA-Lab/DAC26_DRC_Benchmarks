import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon91")


m3_layer = layout.layer(30, 0)

m3_1 = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 200), pya.Point(0, 200)])
top_cell.shapes(m3_layer).insert(m3_1)

m3_2 = pya.Polygon([pya.Point(0, 312), pya.Point(80, 312), pya.Point(80, 512), pya.Point(0, 512)])
top_cell.shapes(m3_layer).insert(m3_2)

layout.write("../gds/Polygon91.gds")
