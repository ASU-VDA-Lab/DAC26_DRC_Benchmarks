import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon18")


fin_layer = layout.layer(2, 0)
fin = pya.Polygon([pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 28), pya.Point(0, 28)])
top_cell.shapes(fin_layer).insert(fin)

layout.write("../gds/Polygon18.gds")
