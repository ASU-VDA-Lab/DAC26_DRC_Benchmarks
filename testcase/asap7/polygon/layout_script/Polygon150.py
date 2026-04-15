import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon150")


m7_layer = layout.layer(70, 0)

m7 = pya.Polygon([pya.Point(0, 0), pya.Point(128, 0), pya.Point(128, 160), pya.Point(0, 160)])
top_cell.shapes(m7_layer).insert(m7)

layout.write("../gds/Polygon150.gds")
