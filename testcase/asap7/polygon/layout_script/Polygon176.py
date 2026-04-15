import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon176")


m9_layer = layout.layer(90, 0)

m9 = pya.Polygon([pya.Point(0, 0), pya.Point(140, 0), pya.Point(140, 400), pya.Point(0, 400)])
top_cell.shapes(m9_layer).insert(m9)

layout.write("../gds/Polygon176.gds")
