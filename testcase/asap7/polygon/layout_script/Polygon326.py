import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon326")


poly = pya.Polygon([ pya.Point(0, 0), pya.Point(2000, 0), pya.Point(2000, 2000), pya.Point(0, 2000), ])
poly.insert_hole([ pya.Point(400, 400), pya.Point(400, 600), pya.Point(832, 600), pya.Point(832, 400), ])
top_cell.shapes(layout.layer(1, 0)).insert(poly)

layout.write("../gds/Polygon326.gds")
