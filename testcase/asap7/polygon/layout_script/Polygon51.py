import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon51")


lig_layer = layout.layer(16, 0)

polygon_lig1 = pya.Polygon([ pya.Point(0, 0), pya.Point(144, 0), pya.Point(144, 72), pya.Point(0, 72), ])
top_cell.shapes(lig_layer).insert(polygon_lig1)

polygon_lig2 = pya.Polygon([ pya.Point(0, 152), pya.Point(200, 152), pya.Point(200, 224), pya.Point(0, 224), ])
top_cell.shapes(lig_layer).insert(polygon_lig2)

layout.write("../gds/Polygon51.gds")
