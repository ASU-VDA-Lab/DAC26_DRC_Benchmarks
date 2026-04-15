import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon85")


m2_layer = layout.layer(20, 0)

top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(0, 256), pya.Point(320, 256), pya.Point(320, 404), pya.Point(0, 404)]))

top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(392, 256), pya.Point(712, 256), pya.Point(712, 404), pya.Point(392, 404)]))

top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(40, 0), pya.Point(360, 0), pya.Point(360, 148), pya.Point(40, 148)]))

top_cell.shapes(m2_layer).insert(pya.Polygon([pya.Point(432, 0), pya.Point(752, 0), pya.Point(752, 148), pya.Point(432, 148)]))

layout.write("../gds/Polygon85.gds")
