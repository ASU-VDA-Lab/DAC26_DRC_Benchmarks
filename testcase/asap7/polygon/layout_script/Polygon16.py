import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon16")


fin_layer = layout.layer(2, 0)
fin1 = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 28), pya.Point(0, 28)])
fin2 = pya.Polygon([pya.Point(0, 88), pya.Point(800, 88), pya.Point(800, 116), pya.Point(0, 116)])
top_cell.shapes(fin_layer).insert(fin1)
top_cell.shapes(fin_layer).insert(fin2)

layout.write("../gds/Polygon16.gds")
