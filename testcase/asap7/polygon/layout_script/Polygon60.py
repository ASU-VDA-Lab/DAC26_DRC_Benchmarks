import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon60")


lisd_layer = layout.layer(17, 0)

lisd1 = pya.Polygon([pya.Point(0, 0), pya.Point(120, 0), pya.Point(120, 120), pya.Point(0, 120)])
top_cell.shapes(lisd_layer).insert(lisd1)

lisd2 = pya.Polygon([pya.Point(0, 220), pya.Point(120, 220), pya.Point(120, 340), pya.Point(0, 340)])
top_cell.shapes(lisd_layer).insert(lisd2)

layout.write("../gds/Polygon60.gds")
