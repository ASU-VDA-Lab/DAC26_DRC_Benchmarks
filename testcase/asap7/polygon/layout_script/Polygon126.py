import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon126")


m6_layer = layout.layer(60, 0)

m6_wide = pya.Polygon([pya.Point(384, 128), pya.Point(864, 128), pya.Point(864, 768), pya.Point(384, 768)])
top_cell.shapes(m6_layer).insert(m6_wide)

m6_track = pya.Polygon([pya.Point(0, 0), pya.Point(192, 0), pya.Point(192, 128), pya.Point(0, 128)])
top_cell.shapes(m6_layer).insert(m6_track)

m6_ref = pya.Polygon([pya.Point(0, 768), pya.Point(192, 768), pya.Point(192, 896), pya.Point(0, 896)])
top_cell.shapes(m6_layer).insert(m6_ref)

layout.write("../gds/Polygon126.gds")
