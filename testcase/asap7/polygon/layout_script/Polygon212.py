import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon212")


active_layer = layout.layer(11, 0)
nselect_layer = layout.layer(12, 0)
sramdrc_layer = layout.layer(99, 0)


active = pya.Polygon([ pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(0, 800), ])
active.insert_hole([ pya.Point(200, 200), pya.Point(200, 308), pya.Point(260, 308), pya.Point(260, 200), ])
top_cell.shapes(active_layer).insert(active)

sramdrc = pya.Polygon([pya.Point(0, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(0, 800)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

nselect = pya.Polygon([pya.Point(-200, -120), pya.Point(1000, -120), pya.Point(1000, 920), pya.Point(-200, 920)])
top_cell.shapes(nselect_layer).insert(nselect)

layout.write("../gds/Polygon212.gds")
