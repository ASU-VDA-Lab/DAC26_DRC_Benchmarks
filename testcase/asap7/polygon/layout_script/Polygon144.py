import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon144")


m7_layer = layout.layer(70, 0)

m7_a = pya.Polygon([pya.Point(0, 0), pya.Point(128, 0), pya.Point(128, 400), pya.Point(0, 400)])
top_cell.shapes(m7_layer).insert(m7_a)

m7_b = pya.Polygon([pya.Point(256, 128), pya.Point(384, 128), pya.Point(384, 528), pya.Point(256, 528)])
top_cell.shapes(m7_layer).insert(m7_b)

layout.write("../gds/Polygon144.gds")
