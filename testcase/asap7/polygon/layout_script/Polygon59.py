import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon59")


lisd_layer = layout.layer(17, 0)

lisd_1 = pya.Polygon([pya.Point(0, 0), pya.Point(140, 0), pya.Point(140, 200), pya.Point(0, 200)])
top_cell.shapes(lisd_layer).insert(lisd_1)

lisd_2 = pya.Polygon([pya.Point(0, 280), pya.Point(200, 280), pya.Point(200, 480), pya.Point(0, 480)])
top_cell.shapes(lisd_layer).insert(lisd_2)

layout.write("../gds/Polygon59.gds")
