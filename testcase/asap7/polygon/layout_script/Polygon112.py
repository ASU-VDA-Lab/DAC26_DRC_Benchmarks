import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon112")


m5_layer = layout.layer(50, 0)

m5_wide = pya.Polygon([pya.Point(96, 384), pya.Point(576, 384), pya.Point(576, 864), pya.Point(96, 864)])
top_cell.shapes(m5_layer).insert(m5_wide)

m5_track = pya.Polygon([pya.Point(0, 0), pya.Point(96, 0), pya.Point(96, 192), pya.Point(0, 192)])
top_cell.shapes(m5_layer).insert(m5_track)

m5_ref = pya.Polygon([pya.Point(768, 0), pya.Point(864, 0), pya.Point(864, 192), pya.Point(768, 192)])
top_cell.shapes(m5_layer).insert(m5_ref)

layout.write("../gds/Polygon112.gds")
