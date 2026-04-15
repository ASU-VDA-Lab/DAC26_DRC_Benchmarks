import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon315")


m8_layer = layout.layer(80, 0)
v8_layer = layout.layer(85, 0)
m9_layer = layout.layer(90, 0)

v8_1 = pya.Polygon([pya.Point(0, 0), pya.Point(160, 0), pya.Point(160, 160), pya.Point(0, 160)])
top_cell.shapes(v8_layer).insert(v8_1)

v8_2 = pya.Polygon([pya.Point(360, 0), pya.Point(520, 0), pya.Point(520, 160), pya.Point(360, 160)])
top_cell.shapes(v8_layer).insert(v8_2)

m8 = pya.Polygon([pya.Point(-80, -80), pya.Point(600, -80), pya.Point(600, 240), pya.Point(-80, 240)])
top_cell.shapes(m8_layer).insert(m8)

m9 = pya.Polygon([pya.Point(-80, -80), pya.Point(600, -80), pya.Point(600, 240), pya.Point(-80, 240)])
top_cell.shapes(m9_layer).insert(m9)

layout.write("../gds/Polygon315.gds")
