import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon140")


m7_layer = layout.layer(70, 0)

m7_wide = pya.Polygon([pya.Point(128, 384), pya.Point(768, 384), pya.Point(768, 864), pya.Point(128, 864)])
top_cell.shapes(m7_layer).insert(m7_wide)

m7_track = pya.Polygon([pya.Point(0, 0), pya.Point(128, 0), pya.Point(128, 192), pya.Point(0, 192)])
top_cell.shapes(m7_layer).insert(m7_track)

m7_ref = pya.Polygon([pya.Point(768, 0), pya.Point(896, 0), pya.Point(896, 192), pya.Point(768, 192)])
top_cell.shapes(m7_layer).insert(m7_ref)

layout.write("../gds/Polygon140.gds")
