import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon61")


lisd_layer = layout.layer(17, 0)

lisd = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 400), pya.Point(0, 400)])
top_cell.shapes(lisd_layer).insert(lisd)

layout.write("../gds/Polygon61.gds")
