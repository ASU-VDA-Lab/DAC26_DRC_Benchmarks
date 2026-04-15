import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon82")


m2_layer = layout.layer(20, 0)

m2_1 = pya.Polygon([pya.Point(0, 0), pya.Point(120, 0), pya.Point(120, 200), pya.Point(0, 200)])
top_cell.shapes(m2_layer).insert(m2_1)

m2_2 = pya.Polygon([pya.Point(20, 312), pya.Point(100, 312), pya.Point(100, 512), pya.Point(20, 512)])
top_cell.shapes(m2_layer).insert(m2_2)

layout.write("../gds/Polygon82.gds")
