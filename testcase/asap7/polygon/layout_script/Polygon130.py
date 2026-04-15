import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon130")


m6_layer = layout.layer(60, 0)

m6_a = pya.Polygon([pya.Point(0, 0), pya.Point(512, 0), pya.Point(512, 128), pya.Point(0, 128)])
top_cell.shapes(m6_layer).insert(m6_a)

m6_b = pya.Polygon([pya.Point(640, 256), pya.Point(1280, 256), pya.Point(1280, 384), pya.Point(640, 384)])
top_cell.shapes(m6_layer).insert(m6_b)

m6_c = pya.Polygon([pya.Point(0, 512), pya.Point(1280, 512), pya.Point(1280, 640), pya.Point(0, 640)])
top_cell.shapes(m6_layer).insert(m6_c)

m6_d = pya.Polygon([pya.Point(0, 1024), pya.Point(256, 1024), pya.Point(256, 1424), pya.Point(0, 1424)])
top_cell.shapes(m6_layer).insert(m6_d)

m6_e = pya.Polygon([pya.Point(128, 1552), pya.Point(384, 1552), pya.Point(384, 1952), pya.Point(128, 1952)])
top_cell.shapes(m6_layer).insert(m6_e)

layout.write("../gds/Polygon130.gds")
