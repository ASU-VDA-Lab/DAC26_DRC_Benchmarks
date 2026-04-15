import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon145")


m7_layer = layout.layer(70, 0)

m7_1a = pya.Polygon([pya.Point(0, 0), pya.Point(400, 0), pya.Point(400, 256), pya.Point(0, 256)])
top_cell.shapes(m7_layer).insert(m7_1a)

m7_1b = pya.Polygon([pya.Point(496, 128), pya.Point(896, 128), pya.Point(896, 384), pya.Point(496, 384)])
top_cell.shapes(m7_layer).insert(m7_1b)

m7_2a = pya.Polygon([pya.Point(0, 640), pya.Point(400, 640), pya.Point(400, 896), pya.Point(0, 896)])
top_cell.shapes(m7_layer).insert(m7_2a)

m7_2b = pya.Polygon([pya.Point(528, 768), pya.Point(928, 768), pya.Point(928, 1024), pya.Point(528, 1024)])
top_cell.shapes(m7_layer).insert(m7_2b)

layout.write("../gds/Polygon145.gds")
