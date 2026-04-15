import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon90")


m3_layer = layout.layer(30, 0)

m3_1 = pya.Polygon([pya.Point(0, 0), pya.Point(120, 0), pya.Point(120, 200), pya.Point(0, 200)])
top_cell.shapes(m3_layer).insert(m3_1)

m3_2 = pya.Polygon([pya.Point(0, 300), pya.Point(120, 300), pya.Point(120, 500), pya.Point(0, 500)])
top_cell.shapes(m3_layer).insert(m3_2)

layout.write("../gds/Polygon90.gds")
