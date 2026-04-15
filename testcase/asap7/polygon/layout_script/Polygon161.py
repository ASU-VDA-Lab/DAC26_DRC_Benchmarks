import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon161")


m8_layer = layout.layer(80, 0)

m8_polygon = pya.Polygon([
    pya.Point(0, 0), pya.Point(800, 0),
    pya.Point(800, 400), pya.Point(472, 400),
    pya.Point(472, 7604), pya.Point(800, 7604),
    pya.Point(800, 8000), pya.Point(0, 8000),
    pya.Point(0, 7604), pya.Point(328, 7604),
    pya.Point(328, 400), pya.Point(0, 400),
])
top_cell.shapes(m8_layer).insert(m8_polygon)

layout.write("../gds/Polygon161.gds")
