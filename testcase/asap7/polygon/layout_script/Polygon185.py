import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon185")


nselect_layer = layout.layer(12, 0)
pselect_layer = layout.layer(13, 0)

nselect = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(0, 800)])
top_cell.shapes(nselect_layer).insert(nselect)

pselect = pya.Polygon([pya.Point(400, 0), pya.Point(1200, 0), pya.Point(1200, 800), pya.Point(400, 800)])
top_cell.shapes(pselect_layer).insert(pselect)

layout.write("../gds/Polygon185.gds")
