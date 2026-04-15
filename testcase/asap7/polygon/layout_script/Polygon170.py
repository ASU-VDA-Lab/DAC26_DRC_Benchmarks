import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon170")


m9_layer = layout.layer(90, 0)

m9_1 = pya.Polygon([pya.Point(0, 0), pya.Point(384, 0), pya.Point(384, 316), pya.Point(0, 316)])
top_cell.shapes(m9_layer).insert(m9_1)

m9_2 = pya.Polygon([pya.Point(560, 0), pya.Point(944, 0), pya.Point(944, 316), pya.Point(560, 316)])
top_cell.shapes(m9_layer).insert(m9_2)

layout.write("../gds/Polygon170.gds")
