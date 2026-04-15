import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon331")

poly = pya.Polygon([pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 800), pya.Point(0, 800)])
top_cell.shapes(layout.layer(1, 0)).insert(poly)

layout.write("../gds/Polygon331.gds")
