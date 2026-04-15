import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon321")


m9_layer = layout.layer(90, 0)
v9_layer = layout.layer(95, 0)
pad_layer = layout.layer(96, 0)

v9_1 = pya.Polygon([pya.Point(0, 0), pya.Point(160, 0), pya.Point(160, 160), pya.Point(0, 160)])
top_cell.shapes(v9_layer).insert(v9_1)

v9_2 = pya.Polygon([pya.Point(360, 0), pya.Point(520, 0), pya.Point(520, 160), pya.Point(360, 160)])
top_cell.shapes(v9_layer).insert(v9_2)

m9 = pya.Polygon([pya.Point(-80, -80), pya.Point(600, -80), pya.Point(600, 240), pya.Point(-80, 240)])
top_cell.shapes(m9_layer).insert(m9)

pad = pya.Polygon([pya.Point(-80, -80), pya.Point(600, -80), pya.Point(600, 240), pya.Point(-80, 240)])
top_cell.shapes(pad_layer).insert(pad)

layout.write("../gds/Polygon321.gds")
