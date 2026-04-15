import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon312")


m8_layer = layout.layer(80, 0)
v8_layer = layout.layer(85, 0)
m9_layer = layout.layer(90, 0)

v8 = pya.Polygon([pya.Point(0, 0), pya.Point(160, 0), pya.Point(160, 160), pya.Point(0, 160)])
top_cell.shapes(v8_layer).insert(v8)

m8 = pya.Polygon([pya.Point(40, -80), pya.Point(240, -80), pya.Point(240, 240), pya.Point(40, 240)])
top_cell.shapes(m8_layer).insert(m8)

m9 = pya.Polygon([pya.Point(-80, -80), pya.Point(240, -80), pya.Point(240, 240), pya.Point(-80, 240)])
top_cell.shapes(m9_layer).insert(m9)

layout.write("../gds/Polygon312.gds")
