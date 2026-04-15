import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell73")

polygon_N1_0 = pya.Polygon([ pya.Point(16, 140), pya.Point(1200, 140), pya.Point(1200, 212), pya.Point(16, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(88, 1148), pya.Point(552, 1148), pya.Point(552, 1220), pya.Point(88, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N1_2 = pya.Polygon([ pya.Point(448, 716), pya.Point(624, 716), pya.Point(624, 788), pya.Point(448, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_2)

polygon_N10_3 = pya.Polygon([ pya.Point(736, 284), pya.Point(1272, 284), pya.Point(1272, 356), pya.Point(736, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_3)

polygon_N10_4 = pya.Polygon([ pya.Point(1024, 716), pya.Point(1272, 716), pya.Point(1272, 788), pya.Point(1024, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_4)

polygon_N11_5 = pya.Polygon([ pya.Point(880, 428), pya.Point(1632, 428), pya.Point(1632, 500), pya.Point(880, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_5)

polygon_N12_6 = pya.Polygon([ pya.Point(1312, 140), pya.Point(1488, 140), pya.Point(1488, 212), pya.Point(1312, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_6)

polygon_N13_7 = pya.Polygon([ pya.Point(1528, -4), pya.Point(1704, -4), pya.Point(1704, 68), pya.Point(1528, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_7)

polygon_N2_8 = pya.Polygon([ pya.Point(736, -4), pya.Point(912, -4), pya.Point(912, 68), pya.Point(736, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_8)

polygon_N2_9 = pya.Polygon([ pya.Point(736, 572), pya.Point(1704, 572), pya.Point(1704, 644), pya.Point(736, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_9)

polygon_N2_10 = pya.Polygon([ pya.Point(736, 1148), pya.Point(912, 1148), pya.Point(912, 1220), pya.Point(736, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_10)

polygon_N2_11 = pya.Polygon([ pya.Point(1528, 716), pya.Point(1704, 716), pya.Point(1704, 788), pya.Point(1528, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_11)

polygon_N3_12 = pya.Polygon([ pya.Point(16, 860), pya.Point(1128, 860), pya.Point(1128, 932), pya.Point(16, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_12)

polygon_N3_13 = pya.Polygon([ pya.Point(952, -4), pya.Point(1128, -4), pya.Point(1128, 68), pya.Point(952, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_13)

polygon_N3_14 = pya.Polygon([ pya.Point(952, 1148), pya.Point(1632, 1148), pya.Point(1632, 1220), pya.Point(952, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_14)

polygon_N4_15 = pya.Polygon([ pya.Point(160, 284), pya.Point(696, 284), pya.Point(696, 356), pya.Point(160, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_15)

polygon_N4_16 = pya.Polygon([ pya.Point(160, 1004), pya.Point(480, 1004), pya.Point(480, 1076), pya.Point(160, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_16)

polygon_N5_17 = pya.Polygon([ pya.Point(16, -4), pya.Point(696, -4), pya.Point(696, 68), pya.Point(16, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_17)

polygon_N5_18 = pya.Polygon([ pya.Point(16, 716), pya.Point(192, 716), pya.Point(192, 788), pya.Point(16, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_18)

polygon_N5_19 = pya.Polygon([ pya.Point(520, 1004), pya.Point(696, 1004), pya.Point(696, 1076), pya.Point(520, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_19)

polygon_N6_20 = pya.Polygon([ pya.Point(736, 1004), pya.Point(1416, 1004), pya.Point(1416, 1076), pya.Point(736, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_20)

polygon_N7_21 = pya.Polygon([ pya.Point(1240, 860), pya.Point(1488, 860), pya.Point(1488, 932), pya.Point(1240, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_21)

polygon_N8_22 = pya.Polygon([ pya.Point(304, 428), pya.Point(624, 428), pya.Point(624, 500), pya.Point(304, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_22)

polygon_N8_23 = pya.Polygon([ pya.Point(232, 716), pya.Point(408, 716), pya.Point(408, 788), pya.Point(232, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_23)

polygon_N9_24 = pya.Polygon([ pya.Point(1168, -4), pya.Point(1488, -4), pya.Point(1488, 68), pya.Point(1168, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_24)

polygon_N9_25 = pya.Polygon([ pya.Point(808, 716), pya.Point(984, 716), pya.Point(984, 788), pya.Point(808, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_25)

polygon_N1_26 = pya.Polygon([ pya.Point(472, 80), pya.Point(544, 80), pya.Point(544, 1264), pya.Point(472, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_26)

polygon_N10_27 = pya.Polygon([ pya.Point(1192, 224), pya.Point(1264, 224), pya.Point(1264, 832), pya.Point(1192, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_27)

polygon_N12_28 = pya.Polygon([ pya.Point(1336, 80), pya.Point(1408, 80), pya.Point(1408, 256), pya.Point(1336, 256), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N12_28)

polygon_N13_29 = pya.Polygon([ pya.Point(1624, -64), pya.Point(1696, -64), pya.Point(1696, 112), pya.Point(1624, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N13_29)

polygon_N2_30 = pya.Polygon([ pya.Point(760, -64), pya.Point(832, -64), pya.Point(832, 1264), pya.Point(760, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_30)

polygon_N2_31 = pya.Polygon([ pya.Point(1624, 512), pya.Point(1696, 512), pya.Point(1696, 832), pya.Point(1624, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_31)

polygon_N3_32 = pya.Polygon([ pya.Point(1048, -64), pya.Point(1120, -64), pya.Point(1120, 1264), pya.Point(1048, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_32)

polygon_N4_33 = pya.Polygon([ pya.Point(184, 224), pya.Point(256, 224), pya.Point(256, 1120), pya.Point(184, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_33)

polygon_N5_34 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 832), pya.Point(40, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_34)

polygon_N5_35 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 1120), pya.Point(616, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_35)

polygon_N7_36 = pya.Polygon([ pya.Point(1336, 800), pya.Point(1408, 800), pya.Point(1408, 976), pya.Point(1336, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_36)

polygon_N8_37 = pya.Polygon([ pya.Point(328, 368), pya.Point(400, 368), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_37)

polygon_N9_38 = pya.Polygon([ pya.Point(904, -64), pya.Point(976, -64), pya.Point(976, 832), pya.Point(904, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_38)

polygon_N9_39 = pya.Polygon([ pya.Point(1192, -64), pya.Point(1264, -64), pya.Point(1264, 112), pya.Point(1192, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_39)

polygon_N9_40 = pya.Polygon([ pya.Point(848, -4), pya.Point(1392, -4), pya.Point(1392, 68), pya.Point(848, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(20, 0))).insert(polygon_N9_40)

polygon_N1_41 = pya.Polygon([ pya.Point(472, 1148), pya.Point(544, 1148), pya.Point(544, 1220), pya.Point(472, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_41)

polygon_N1_42 = pya.Polygon([ pya.Point(472, 716), pya.Point(544, 716), pya.Point(544, 788), pya.Point(472, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_42)

polygon_N1_43 = pya.Polygon([ pya.Point(472, 140), pya.Point(544, 140), pya.Point(544, 212), pya.Point(472, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_43)

polygon_N2_44 = pya.Polygon([ pya.Point(760, 1148), pya.Point(832, 1148), pya.Point(832, 1220), pya.Point(760, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_44)

polygon_N2_45 = pya.Polygon([ pya.Point(1624, 716), pya.Point(1696, 716), pya.Point(1696, 788), pya.Point(1624, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_45)

polygon_N2_46 = pya.Polygon([ pya.Point(760, 572), pya.Point(832, 572), pya.Point(832, 644), pya.Point(760, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_46)

polygon_N2_47 = pya.Polygon([ pya.Point(1624, 572), pya.Point(1696, 572), pya.Point(1696, 644), pya.Point(1624, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_47)

polygon_N2_48 = pya.Polygon([ pya.Point(760, -4), pya.Point(832, -4), pya.Point(832, 68), pya.Point(760, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_48)

polygon_N3_49 = pya.Polygon([ pya.Point(1048, 1148), pya.Point(1120, 1148), pya.Point(1120, 1220), pya.Point(1048, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_49)

polygon_N3_50 = pya.Polygon([ pya.Point(1048, 860), pya.Point(1120, 860), pya.Point(1120, 932), pya.Point(1048, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_50)

polygon_N3_51 = pya.Polygon([ pya.Point(1048, -4), pya.Point(1120, -4), pya.Point(1120, 68), pya.Point(1048, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_51)

polygon_N4_52 = pya.Polygon([ pya.Point(184, 1004), pya.Point(256, 1004), pya.Point(256, 1076), pya.Point(184, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_52)

polygon_N4_53 = pya.Polygon([ pya.Point(184, 284), pya.Point(256, 284), pya.Point(256, 356), pya.Point(184, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_53)

polygon_N5_54 = pya.Polygon([ pya.Point(616, 1004), pya.Point(688, 1004), pya.Point(688, 1076), pya.Point(616, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_54)

polygon_N5_55 = pya.Polygon([ pya.Point(40, 716), pya.Point(112, 716), pya.Point(112, 788), pya.Point(40, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_55)

polygon_N5_56 = pya.Polygon([ pya.Point(40, -4), pya.Point(112, -4), pya.Point(112, 68), pya.Point(40, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_56)

polygon_N5_57 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_57)

polygon_N7_58 = pya.Polygon([ pya.Point(1336, 860), pya.Point(1408, 860), pya.Point(1408, 932), pya.Point(1336, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_58)

polygon_N8_59 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_59)

polygon_N8_60 = pya.Polygon([ pya.Point(328, 428), pya.Point(400, 428), pya.Point(400, 500), pya.Point(328, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_60)

polygon_N9_61 = pya.Polygon([ pya.Point(904, 716), pya.Point(976, 716), pya.Point(976, 788), pya.Point(904, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_61)

polygon_N9_62 = pya.Polygon([ pya.Point(1192, -4), pya.Point(1264, -4), pya.Point(1264, 68), pya.Point(1192, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_62)

polygon_N10_63 = pya.Polygon([ pya.Point(1192, 716), pya.Point(1264, 716), pya.Point(1264, 788), pya.Point(1192, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_63)

polygon_N10_64 = pya.Polygon([ pya.Point(1192, 284), pya.Point(1264, 284), pya.Point(1264, 356), pya.Point(1192, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_64)

polygon_N12_65 = pya.Polygon([ pya.Point(1336, 140), pya.Point(1408, 140), pya.Point(1408, 212), pya.Point(1336, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_65)

polygon_N13_66 = pya.Polygon([ pya.Point(1624, -4), pya.Point(1696, -4), pya.Point(1696, 68), pya.Point(1624, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_66)

polygon_N9_67 = pya.Polygon([ pya.Point(904, -4), pya.Point(976, -4), pya.Point(976, 68), pya.Point(904, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(21, 0))).insert(polygon_N9_67)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1704, -64), pya.Point(1704, 1264), pya.Point(16, 1264)]))

layout.write("../gds/Cell73.gds")
