import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon329")


nwell_layer = layout.layer(1, 0)

poly1 = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(0, 800)])
top_cell.shapes(nwell_layer).insert(poly1)

poly2 = pya.Polygon([pya.Point(1200, 0), pya.Point(2000, 0), pya.Point(2000, 800), pya.Point(1200, 800)])
top_cell.shapes(nwell_layer).insert(poly2)

layout.write("../gds/Polygon329.gds")
