import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon317")


m8_layer = layout.layer(80, 0)
v8_layer = layout.layer(85, 0)
m9_layer = layout.layer(90, 0)

v8 = pya.Polygon([pya.Point(0, 0), pya.Point(200, 0), pya.Point(200, 200), pya.Point(0, 200)])
top_cell.shapes(v8_layer).insert(v8)

m8 = pya.Polygon([pya.Point(-80, -80), pya.Point(280, -80), pya.Point(280, 280), pya.Point(-80, 280)])
top_cell.shapes(m8_layer).insert(m8)

m9 = pya.Polygon([pya.Point(-80, -80), pya.Point(280, -80), pya.Point(280, 280), pya.Point(-80, 280)])
top_cell.shapes(m9_layer).insert(m9)

layout.write("../gds/Polygon317.gds")
