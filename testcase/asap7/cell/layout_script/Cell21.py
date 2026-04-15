import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell21")

polygon_N1_0 = pya.Polygon([ pya.Point(16, 1004), pya.Point(1056, 1004), pya.Point(1056, 1076), pya.Point(16, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(736, 428), pya.Point(1056, 428), pya.Point(1056, 500), pya.Point(736, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N2_2 = pya.Polygon([ pya.Point(88, 284), pya.Point(984, 284), pya.Point(984, 356), pya.Point(88, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_2)

polygon_N2_3 = pya.Polygon([ pya.Point(232, 860), pya.Point(984, 860), pya.Point(984, 932), pya.Point(232, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_3)

polygon_N3_4 = pya.Polygon([ pya.Point(592, 572), pya.Point(1272, 572), pya.Point(1272, 644), pya.Point(592, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_4)

polygon_N3_5 = pya.Polygon([ pya.Point(592, 716), pya.Point(768, 716), pya.Point(768, 788), pya.Point(592, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_5)

polygon_N3_6 = pya.Polygon([ pya.Point(1096, 860), pya.Point(1272, 860), pya.Point(1272, 932), pya.Point(1096, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_6)

polygon_N4_7 = pya.Polygon([ pya.Point(160, -4), pya.Point(1128, -4), pya.Point(1128, 68), pya.Point(160, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_7)

polygon_N4_8 = pya.Polygon([ pya.Point(88, 716), pya.Point(264, 716), pya.Point(264, 788), pya.Point(88, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_8)

polygon_N4_9 = pya.Polygon([ pya.Point(808, 716), pya.Point(1128, 716), pya.Point(1128, 788), pya.Point(808, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_9)

polygon_N5_10 = pya.Polygon([ pya.Point(160, 140), pya.Point(552, 140), pya.Point(552, 212), pya.Point(160, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_10)

polygon_N5_11 = pya.Polygon([ pya.Point(304, 716), pya.Point(480, 716), pya.Point(480, 788), pya.Point(304, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_11)

polygon_N6_12 = pya.Polygon([ pya.Point(664, 140), pya.Point(1200, 140), pya.Point(1200, 212), pya.Point(664, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_12)

polygon_N1_13 = pya.Polygon([ pya.Point(760, 368), pya.Point(832, 368), pya.Point(832, 1120), pya.Point(760, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_13)

polygon_N2_14 = pya.Polygon([ pya.Point(904, 224), pya.Point(976, 224), pya.Point(976, 976), pya.Point(904, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_14)

polygon_N3_15 = pya.Polygon([ pya.Point(616, 512), pya.Point(688, 512), pya.Point(688, 832), pya.Point(616, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_15)

polygon_N3_16 = pya.Polygon([ pya.Point(1192, 512), pya.Point(1264, 512), pya.Point(1264, 976), pya.Point(1192, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_16)

polygon_N4_17 = pya.Polygon([ pya.Point(184, -64), pya.Point(256, -64), pya.Point(256, 832), pya.Point(184, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_17)

polygon_N4_18 = pya.Polygon([ pya.Point(1048, -64), pya.Point(1120, -64), pya.Point(1120, 832), pya.Point(1048, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_18)

polygon_N5_19 = pya.Polygon([ pya.Point(328, 80), pya.Point(400, 80), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_19)

polygon_N6_20 = pya.Polygon([ pya.Point(760, 80), pya.Point(832, 80), pya.Point(832, 256), pya.Point(760, 256), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_20)

polygon_N1_21 = pya.Polygon([ pya.Point(760, 1004), pya.Point(832, 1004), pya.Point(832, 1076), pya.Point(760, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_21)

polygon_N1_22 = pya.Polygon([ pya.Point(760, 428), pya.Point(832, 428), pya.Point(832, 500), pya.Point(760, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_22)

polygon_N2_23 = pya.Polygon([ pya.Point(904, 860), pya.Point(976, 860), pya.Point(976, 932), pya.Point(904, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_23)

polygon_N2_24 = pya.Polygon([ pya.Point(904, 284), pya.Point(976, 284), pya.Point(976, 356), pya.Point(904, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_24)

polygon_N3_25 = pya.Polygon([ pya.Point(1192, 860), pya.Point(1264, 860), pya.Point(1264, 932), pya.Point(1192, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_25)

polygon_N3_26 = pya.Polygon([ pya.Point(616, 716), pya.Point(688, 716), pya.Point(688, 788), pya.Point(616, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_26)

polygon_N3_27 = pya.Polygon([ pya.Point(616, 572), pya.Point(688, 572), pya.Point(688, 644), pya.Point(616, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_27)

polygon_N3_28 = pya.Polygon([ pya.Point(1192, 572), pya.Point(1264, 572), pya.Point(1264, 644), pya.Point(1192, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_28)

polygon_N4_29 = pya.Polygon([ pya.Point(184, 716), pya.Point(256, 716), pya.Point(256, 788), pya.Point(184, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_29)

polygon_N4_30 = pya.Polygon([ pya.Point(1048, 716), pya.Point(1120, 716), pya.Point(1120, 788), pya.Point(1048, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_30)

polygon_N4_31 = pya.Polygon([ pya.Point(184, -4), pya.Point(256, -4), pya.Point(256, 68), pya.Point(184, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_31)

polygon_N4_32 = pya.Polygon([ pya.Point(1048, -4), pya.Point(1120, -4), pya.Point(1120, 68), pya.Point(1048, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_32)

polygon_N5_33 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_33)

polygon_N5_34 = pya.Polygon([ pya.Point(328, 140), pya.Point(400, 140), pya.Point(400, 212), pya.Point(328, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_34)

polygon_N6_35 = pya.Polygon([ pya.Point(760, 140), pya.Point(832, 140), pya.Point(832, 212), pya.Point(760, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_35)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1272, -64), pya.Point(1272, 1120), pya.Point(16, 1120)]))

layout.write("../gds/Cell21.gds")
