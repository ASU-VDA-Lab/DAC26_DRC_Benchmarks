import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon163")


m8_layer = layout.layer(80, 0)

m8 = pya.Polygon([ pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 5600), pya.Point(280, 5600), pya.Point(280, 8800), pya.Point(0, 8800), ])
top_cell.shapes(m8_layer).insert(m8)

layout.write("../gds/Polygon163.gds")
