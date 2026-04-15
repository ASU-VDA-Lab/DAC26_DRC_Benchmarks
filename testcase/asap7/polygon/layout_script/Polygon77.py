import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon77")


m2_layer = layout.layer(20, 0)

m2 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 108), pya.Point(0, 108)])
top_cell.shapes(m2_layer).insert(m2)

layout.write("../gds/Polygon77.gds")
