import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon143")


m7_layer = layout.layer(70, 0)

m7_1 = pya.Polygon([pya.Point(0, 0), pya.Point(384, 0), pya.Point(384, 192), pya.Point(0, 192)])
top_cell.shapes(m7_layer).insert(m7_1)

m7_2 = pya.Polygon([pya.Point(416, 320), pya.Point(800, 320), pya.Point(800, 512), pya.Point(416, 512)])
top_cell.shapes(m7_layer).insert(m7_2)

layout.write("../gds/Polygon143.gds")
