import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon17")


fin_layer = layout.layer(2, 0)
fin = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 40), pya.Point(0, 40)])
top_cell.shapes(fin_layer).insert(fin)

layout.write("../gds/Polygon17.gds")
