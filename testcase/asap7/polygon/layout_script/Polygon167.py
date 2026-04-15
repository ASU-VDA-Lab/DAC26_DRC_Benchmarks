import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon167")


m9_layer = layout.layer(90, 0)

m9 = pya.Polygon([ pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 360), pya.Point(280, 360), pya.Point(280, 400), pya.Point(0, 400), ])
top_cell.shapes(m9_layer).insert(m9)

layout.write("../gds/Polygon167.gds")
