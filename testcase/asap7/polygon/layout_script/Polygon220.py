import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Polygon220")


lisd_layer = layout.layer(17, 0)
sramdrc_layer = layout.layer(99, 0)

lisd1 = pya.Polygon([pya.Point(0, 0), pya.Point(120, 0), pya.Point(120, 120), pya.Point(0, 120)])
top_cell.shapes(lisd_layer).insert(lisd1)

lisd2 = pya.Polygon([pya.Point(0, 220), pya.Point(120, 220), pya.Point(120, 340), pya.Point(0, 340)])
top_cell.shapes(lisd_layer).insert(lisd2)

sramdrc = pya.Polygon([pya.Point(-40, -40), pya.Point(160, -40), pya.Point(160, 380), pya.Point(-40, 380)])
top_cell.shapes(sramdrc_layer).insert(sramdrc)

layout.write("../gds/Polygon220.gds")
