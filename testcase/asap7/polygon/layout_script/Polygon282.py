import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon282")


m4_layer = layout.layer(40, 0)
m5_layer = layout.layer(50, 0)
v4_layer = layout.layer(45, 0)

m5 = pya.Polygon([pya.Point(-44, 0), pya.Point(400, 0), pya.Point(400, 192), pya.Point(-44, 192)])
top_cell.shapes(m5_layer).insert(m5)

v4 = pya.Polygon([pya.Point(0, 48), pya.Point(96, 48), pya.Point(96, 144), pya.Point(0, 144)])
top_cell.shapes(v4_layer).insert(v4)

m4 = pya.Polygon([pya.Point(-44, 4), pya.Point(140, 4), pya.Point(140, 188), pya.Point(-44, 188)])
top_cell.shapes(m4_layer).insert(m4)

layout.write("../gds/Polygon282.gds")
