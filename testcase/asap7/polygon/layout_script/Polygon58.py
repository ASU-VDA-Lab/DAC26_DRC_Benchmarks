import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon58")


lisd_layer = layout.layer(17, 0)

lisd1 = pya.Polygon([pya.Point(0, 0), pya.Point(200, 0), pya.Point(200, 200), pya.Point(0, 200)])
top_cell.shapes(lisd_layer).insert(lisd1)

lisd2 = pya.Polygon([pya.Point(256, 0), pya.Point(456, 0), pya.Point(456, 200), pya.Point(256, 200)])
top_cell.shapes(lisd_layer).insert(lisd2)

layout.write("../gds/Polygon58.gds")
