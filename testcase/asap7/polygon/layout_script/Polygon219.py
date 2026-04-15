import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon219")


lisd_layer = layout.layer(17, 0)
sramdrc_layer = layout.layer(99, 0)

lisd = pya.Polygon([pya.Point(0, 0), pya.Point(120, 0), pya.Point(120, 200), pya.Point(0, 200)])
top_cell.shapes(lisd_layer).insert(lisd)

sramdrc = pya.Polygon([pya.Point(120, 0), pya.Point(800, 0), pya.Point(800, 800), pya.Point(120, 800)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

layout.write("../gds/Polygon219.gds")
