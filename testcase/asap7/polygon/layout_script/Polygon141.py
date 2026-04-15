import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon141")


m7_layer = layout.layer(70, 0)

m7_1 = pya.Polygon([pya.Point(0, 0), pya.Point(128, 0), pya.Point(128, 192), pya.Point(0, 192)])
top_cell.shapes(m7_layer).insert(m7_1)

m7_2 = pya.Polygon([pya.Point(240, 0), pya.Point(368, 0), pya.Point(368, 192), pya.Point(240, 192)])
top_cell.shapes(m7_layer).insert(m7_2)

layout.write("../gds/Polygon141.gds")
