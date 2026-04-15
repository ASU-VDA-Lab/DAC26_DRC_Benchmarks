import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon172")


m9_layer = layout.layer(90, 0)

m9_1 = pya.Polygon([pya.Point(0, 0), pya.Point(360, 0), pya.Point(360, 800), pya.Point(0, 800)])
top_cell.shapes(m9_layer).insert(m9_1)

m9_2 = pya.Polygon([pya.Point(640, 0), pya.Point(1000, 0), pya.Point(1000, 800), pya.Point(640, 800)])
top_cell.shapes(m9_layer).insert(m9_2)

layout.write("../gds/Polygon172.gds")
