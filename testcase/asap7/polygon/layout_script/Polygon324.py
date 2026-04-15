import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon324")


lvt_layer = layout.layer(98, 0)
slvt_layer = layout.layer(97, 0)

lvt = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(0, 800)])
top_cell.shapes(lvt_layer).insert(lvt)

slvt = pya.Polygon([pya.Point(400, 0), pya.Point(1200, 0), pya.Point(1200, 800), pya.Point(400, 800)])
top_cell.shapes(slvt_layer).insert(slvt)

layout.write("../gds/Polygon324.gds")
