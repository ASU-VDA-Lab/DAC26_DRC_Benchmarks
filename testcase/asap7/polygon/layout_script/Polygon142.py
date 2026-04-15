import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon142")


m7_layer = layout.layer(70, 0)

m7_1 = pya.Polygon([pya.Point(0, 0), pya.Point(256, 0), pya.Point(256, 192), pya.Point(0, 192)])
top_cell.shapes(m7_layer).insert(m7_1)

m7_2 = pya.Polygon([pya.Point(0, 320), pya.Point(256, 320), pya.Point(256, 512), pya.Point(0, 512)])
top_cell.shapes(m7_layer).insert(m7_2)

layout.write("../gds/Polygon142.gds")
