import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon175")


m9_layer = layout.layer(90, 0)

m9_1 = pya.Polygon([pya.Point(0, 0), pya.Point(4800, 0), pya.Point(4800, 4800), pya.Point(0, 4800)])
top_cell.shapes(m9_layer).insert(m9_1)

m9_2 = pya.Polygon([pya.Point(8000, 0), pya.Point(12800, 0), pya.Point(12800, 4800), pya.Point(8000, 4800)])
top_cell.shapes(m9_layer).insert(m9_2)

layout.write("../gds/Polygon175.gds")
