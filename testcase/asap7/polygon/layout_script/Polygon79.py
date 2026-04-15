import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon79")


m2_layer = layout.layer(20, 0)

m2_1 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 120), pya.Point(0, 120)])
top_cell.shapes(m2_layer).insert(m2_1)

m2_2 = pya.Polygon([pya.Point(152, 0), pya.Point(224, 0), pya.Point(224, 200), pya.Point(152, 200)])
top_cell.shapes(m2_layer).insert(m2_2)

layout.write("../gds/Polygon79.gds")
