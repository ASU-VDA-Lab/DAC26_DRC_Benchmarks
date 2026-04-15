import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon216")


lig_layer = layout.layer(16, 0)
sramdrc_layer = layout.layer(99, 0)

lig = pya.Polygon([pya.Point(0, 0), pya.Point(80, 0), pya.Point(80, 200), pya.Point(0, 200)])
top_cell.shapes(lig_layer).insert(lig)

sramdrc = pya.Polygon([pya.Point(80, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(80, 800)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

layout.write("../gds/Polygon216.gds")
