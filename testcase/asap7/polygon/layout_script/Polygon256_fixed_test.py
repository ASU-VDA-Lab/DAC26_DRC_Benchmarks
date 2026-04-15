import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon256")


v1_layer = layout.layer(21, 0)
m1_layer = layout.layer(19, 0)
m2_layer = layout.layer(20, 0)

# V1: flush with M2 in X direction (left/right edges coincident with M2)
# satisfies V1.M2.AUX.2 (2 coincident edges with M2)
# V1 x: -12 to 84 (matches M2 x extent), y: 0 to 72
v1 = pya.Polygon([pya.Point(-12, 0), pya.Point(84, 0), pya.Point(84, 72), pya.Point(-12, 72)])
top_cell.shapes(v1_layer).insert(v1)

m1 = pya.Polygon([pya.Point(-20, -20), pya.Point(92, -20), pya.Point(92, 92), pya.Point(-20, 92)])
top_cell.shapes(m1_layer).insert(m1)

# M2: expanded in Y to give 20 dbu (5 nm) enclosure above and below V1
# satisfies V1.M2.EN.2 (5 nm enclosure on top/bottom; 0 nm flush on left/right is allowed)
# M2 x: -12 to 84 (flush with V1 left/right), y: -20 to 92
m2 = pya.Polygon([pya.Point(-12, -20), pya.Point(84, -20), pya.Point(84, 92), pya.Point(-12, 92)])
top_cell.shapes(m2_layer).insert(m2)

layout.write("../gds/Polygon256.gds")
