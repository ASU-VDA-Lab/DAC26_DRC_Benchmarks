import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon78")


m2_layer = layout.layer(20, 0)

m2_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 200), pya.Point(0, 200)])
top_cell.shapes(m2_layer).insert(m2_1)

m2_2 = pya.Polygon([pya.Point(128, 0), pya.Point(200, 0), pya.Point(200, 200), pya.Point(128, 200)])
top_cell.shapes(m2_layer).insert(m2_2)

layout.write("../gds/Polygon78.gds")
