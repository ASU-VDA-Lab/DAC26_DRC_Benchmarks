import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon138")


m7_layer = layout.layer(70, 0)

m7_valid = pya.Polygon([pya.Point(0, 0), pya.Point(128, 0), pya.Point(128, 192), pya.Point(0, 192)])
top_cell.shapes(m7_layer).insert(m7_valid)

m7_offtrack = pya.Polygon([pya.Point(384, 0), pya.Point(512, 0), pya.Point(512, 192), pya.Point(384, 192)])
top_cell.shapes(m7_layer).insert(m7_offtrack)

layout.write("../gds/Polygon138.gds")
