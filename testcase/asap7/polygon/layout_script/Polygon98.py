import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon98")


m4_layer = layout.layer(40, 0)

m4_wide = pya.Polygon([pya.Point(384, 96), pya.Point(864, 96), pya.Point(864, 576), pya.Point(384, 576)])
top_cell.shapes(m4_layer).insert(m4_wide)

m4_track = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 96), pya.Point(0, 96)])
top_cell.shapes(m4_layer).insert(m4_track)

m4_ref = pya.Polygon([pya.Point(0, 768), pya.Point(192, 768), pya.Point(192, 864), pya.Point(0, 864)])
top_cell.shapes(m4_layer).insert(m4_ref)

layout.write("../gds/Polygon98.gds")
