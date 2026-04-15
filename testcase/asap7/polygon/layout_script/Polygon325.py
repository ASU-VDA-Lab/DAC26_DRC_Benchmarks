import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon325")

poly = pya.Polygon([pya.Point(0, 0), pya.Point(432, 0), pya.Point(432, 200), pya.Point(0, 200)])
top_cell.shapes(layout.layer(1, 0)).insert(poly)

layout.write("../gds/Polygon325.gds")
