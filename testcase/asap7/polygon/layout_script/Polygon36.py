import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon36")


gate_layer = layout.layer(7, 0)
gcut_layer = layout.layer(10, 0)

gate = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 400), pya.Point(0, 400)])
gcut1 = pya.Polygon([pya.Point(-80, 60), pya.Point(160, 60), pya.Point(160, 128), pya.Point(-80, 128)])
gcut2 = pya.Polygon([pya.Point(-80, 220), pya.Point(160, 220), pya.Point(160, 288), pya.Point(-80, 288)])

top_cell.shapes(gate_layer).insert(gate)
top_cell.shapes(gcut_layer).insert(gcut1)
top_cell.shapes(gcut_layer).insert(gcut2)

layout.write("../gds/Polygon36.gds")
