import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon72")


m1_layer = layout.layer(19, 0)

m1_1 = pya.Polygon([pya.Point(0, 0), pya.Point(120, 0), pya.Point(120, 200), pya.Point(0, 200)])
top_cell.shapes(m1_layer).insert(m1_1)

m1_2 = pya.Polygon([pya.Point(0, 300), pya.Point(120, 300), pya.Point(120, 500), pya.Point(0, 500)])
top_cell.shapes(m1_layer).insert(m1_2)

layout.write("../gds/Polygon72.gds")
