import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon240")


v0_layer = layout.layer(18, 0)

v0 = pya.Polygon([pya.Point(0, 0), pya.Point(72, 0), pya.Point(72, 72), pya.Point(0, 72)])
top_cell.shapes(v0_layer).insert(v0)

layout.write("../gds/Polygon240.gds")
