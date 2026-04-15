import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell123")

polygon_N1_0 = pya.Polygon([ pya.Point(16, 1148), pya.Point(840, 1148), pya.Point(840, 1220), pya.Point(16, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N10_1 = pya.Polygon([ pya.Point(1096, 140), pya.Point(1272, 140), pya.Point(1272, 212), pya.Point(1096, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_1)

polygon_N10_2 = pya.Polygon([ pya.Point(808, 860), pya.Point(1272, 860), pya.Point(1272, 932), pya.Point(808, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_2)

polygon_N11_3 = pya.Polygon([ pya.Point(1240, -4), pya.Point(1416, -4), pya.Point(1416, 68), pya.Point(1240, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_3)

polygon_N11_4 = pya.Polygon([ pya.Point(1312, 860), pya.Point(1488, 860), pya.Point(1488, 932), pya.Point(1312, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_4)

polygon_N12_5 = pya.Polygon([ pya.Point(1528, 860), pya.Point(1704, 860), pya.Point(1704, 932), pya.Point(1528, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_5)

polygon_N13_6 = pya.Polygon([ pya.Point(1024, 716), pya.Point(1416, 716), pya.Point(1416, 788), pya.Point(1024, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_6)

polygon_N14_7 = pya.Polygon([ pya.Point(664, 284), pya.Point(1560, 284), pya.Point(1560, 356), pya.Point(664, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_7)

polygon_N14_8 = pya.Polygon([ pya.Point(1456, -4), pya.Point(1704, -4), pya.Point(1704, 68), pya.Point(1456, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_8)

polygon_N14_9 = pya.Polygon([ pya.Point(1456, 716), pya.Point(1632, 716), pya.Point(1632, 788), pya.Point(1456, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_9)

polygon_N15_10 = pya.Polygon([ pya.Point(160, 428), pya.Point(408, 428), pya.Point(408, 500), pya.Point(160, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N15_10)

polygon_N16_11 = pya.Polygon([ pya.Point(880, 428), pya.Point(1488, 428), pya.Point(1488, 500), pya.Point(880, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N16_11)

polygon_N2_12 = pya.Polygon([ pya.Point(448, 140), pya.Point(1056, 140), pya.Point(1056, 212), pya.Point(448, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_12)

polygon_N2_13 = pya.Polygon([ pya.Point(808, 716), pya.Point(984, 716), pya.Point(984, 788), pya.Point(808, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_13)

polygon_N2_14 = pya.Polygon([ pya.Point(880, 1148), pya.Point(1056, 1148), pya.Point(1056, 1220), pya.Point(880, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_14)

polygon_N3_15 = pya.Polygon([ pya.Point(1168, 1148), pya.Point(1416, 1148), pya.Point(1416, 1220), pya.Point(1168, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_15)

polygon_N4_16 = pya.Polygon([ pya.Point(88, 140), pya.Point(408, 140), pya.Point(408, 212), pya.Point(88, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_16)

polygon_N4_17 = pya.Polygon([ pya.Point(232, 716), pya.Point(624, 716), pya.Point(624, 788), pya.Point(232, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_17)

polygon_N4_18 = pya.Polygon([ pya.Point(88, 1004), pya.Point(408, 1004), pya.Point(408, 1076), pya.Point(88, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_18)

polygon_N5_19 = pya.Polygon([ pya.Point(16, -4), pya.Point(192, -4), pya.Point(192, 68), pya.Point(16, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_19)

polygon_N5_20 = pya.Polygon([ pya.Point(16, 284), pya.Point(552, 284), pya.Point(552, 356), pya.Point(16, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_20)

polygon_N5_21 = pya.Polygon([ pya.Point(16, 716), pya.Point(192, 716), pya.Point(192, 788), pya.Point(16, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_21)

polygon_N5_22 = pya.Polygon([ pya.Point(448, 1004), pya.Point(624, 1004), pya.Point(624, 1076), pya.Point(448, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_22)

polygon_N6_23 = pya.Polygon([ pya.Point(232, -4), pya.Point(912, -4), pya.Point(912, 68), pya.Point(232, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_23)

polygon_N6_24 = pya.Polygon([ pya.Point(736, 572), pya.Point(1056, 572), pya.Point(1056, 644), pya.Point(736, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_24)

polygon_N6_25 = pya.Polygon([ pya.Point(736, 1004), pya.Point(984, 1004), pya.Point(984, 1076), pya.Point(736, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_25)

polygon_N7_26 = pya.Polygon([ pya.Point(1024, -4), pya.Point(1200, -4), pya.Point(1200, 68), pya.Point(1024, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_26)

polygon_N7_27 = pya.Polygon([ pya.Point(1024, 1004), pya.Point(1200, 1004), pya.Point(1200, 1076), pya.Point(1024, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_27)

polygon_N8_28 = pya.Polygon([ pya.Point(160, 860), pya.Point(480, 860), pya.Point(480, 932), pya.Point(160, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_28)

polygon_N9_29 = pya.Polygon([ pya.Point(592, 860), pya.Point(768, 860), pya.Point(768, 932), pya.Point(592, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_29)

polygon_N10_30 = pya.Polygon([ pya.Point(1192, 80), pya.Point(1264, 80), pya.Point(1264, 976), pya.Point(1192, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_30)

polygon_N11_31 = pya.Polygon([ pya.Point(1336, -64), pya.Point(1408, -64), pya.Point(1408, 976), pya.Point(1336, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_31)

polygon_N12_32 = pya.Polygon([ pya.Point(1624, 800), pya.Point(1696, 800), pya.Point(1696, 976), pya.Point(1624, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N12_32)

polygon_N14_33 = pya.Polygon([ pya.Point(1480, -64), pya.Point(1552, -64), pya.Point(1552, 832), pya.Point(1480, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N14_33)

polygon_N15_34 = pya.Polygon([ pya.Point(184, 368), pya.Point(256, 368), pya.Point(256, 544), pya.Point(184, 544), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N15_34)

polygon_N2_35 = pya.Polygon([ pya.Point(904, 80), pya.Point(976, 80), pya.Point(976, 1264), pya.Point(904, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_35)

polygon_N4_36 = pya.Polygon([ pya.Point(328, 80), pya.Point(400, 80), pya.Point(400, 1120), pya.Point(328, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_36)

polygon_N5_37 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 832), pya.Point(40, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_37)

polygon_N5_38 = pya.Polygon([ pya.Point(472, 224), pya.Point(544, 224), pya.Point(544, 1120), pya.Point(472, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_38)

polygon_N6_39 = pya.Polygon([ pya.Point(760, -64), pya.Point(832, -64), pya.Point(832, 1120), pya.Point(760, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_39)

polygon_N7_40 = pya.Polygon([ pya.Point(1048, -64), pya.Point(1120, -64), pya.Point(1120, 1120), pya.Point(1048, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_40)

polygon_N8_41 = pya.Polygon([ pya.Point(184, 800), pya.Point(256, 800), pya.Point(256, 976), pya.Point(184, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_41)

polygon_N9_42 = pya.Polygon([ pya.Point(616, 800), pya.Point(688, 800), pya.Point(688, 976), pya.Point(616, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_42)

polygon_N2_43 = pya.Polygon([ pya.Point(904, 1148), pya.Point(976, 1148), pya.Point(976, 1220), pya.Point(904, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_43)

polygon_N2_44 = pya.Polygon([ pya.Point(904, 716), pya.Point(976, 716), pya.Point(976, 788), pya.Point(904, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_44)

polygon_N2_45 = pya.Polygon([ pya.Point(904, 140), pya.Point(976, 140), pya.Point(976, 212), pya.Point(904, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_45)

polygon_N4_46 = pya.Polygon([ pya.Point(328, 1004), pya.Point(400, 1004), pya.Point(400, 1076), pya.Point(328, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_46)

polygon_N4_47 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_47)

polygon_N4_48 = pya.Polygon([ pya.Point(328, 140), pya.Point(400, 140), pya.Point(400, 212), pya.Point(328, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_48)

polygon_N5_49 = pya.Polygon([ pya.Point(472, 1004), pya.Point(544, 1004), pya.Point(544, 1076), pya.Point(472, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_49)

polygon_N5_50 = pya.Polygon([ pya.Point(40, 716), pya.Point(112, 716), pya.Point(112, 788), pya.Point(40, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_50)

polygon_N5_51 = pya.Polygon([ pya.Point(40, 284), pya.Point(112, 284), pya.Point(112, 356), pya.Point(40, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_51)

polygon_N5_52 = pya.Polygon([ pya.Point(472, 284), pya.Point(544, 284), pya.Point(544, 356), pya.Point(472, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_52)

polygon_N5_53 = pya.Polygon([ pya.Point(40, -4), pya.Point(112, -4), pya.Point(112, 68), pya.Point(40, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_53)

polygon_N6_54 = pya.Polygon([ pya.Point(760, 1004), pya.Point(832, 1004), pya.Point(832, 1076), pya.Point(760, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_54)

polygon_N6_55 = pya.Polygon([ pya.Point(760, 572), pya.Point(832, 572), pya.Point(832, 644), pya.Point(760, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_55)

polygon_N6_56 = pya.Polygon([ pya.Point(760, -4), pya.Point(832, -4), pya.Point(832, 68), pya.Point(760, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_56)

polygon_N7_57 = pya.Polygon([ pya.Point(1048, 1004), pya.Point(1120, 1004), pya.Point(1120, 1076), pya.Point(1048, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_57)

polygon_N7_58 = pya.Polygon([ pya.Point(1048, -4), pya.Point(1120, -4), pya.Point(1120, 68), pya.Point(1048, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_58)

polygon_N8_59 = pya.Polygon([ pya.Point(184, 860), pya.Point(256, 860), pya.Point(256, 932), pya.Point(184, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_59)

polygon_N9_60 = pya.Polygon([ pya.Point(616, 860), pya.Point(688, 860), pya.Point(688, 932), pya.Point(616, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_60)

polygon_N10_61 = pya.Polygon([ pya.Point(1192, 860), pya.Point(1264, 860), pya.Point(1264, 932), pya.Point(1192, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_61)

polygon_N10_62 = pya.Polygon([ pya.Point(1192, 140), pya.Point(1264, 140), pya.Point(1264, 212), pya.Point(1192, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_62)

polygon_N11_63 = pya.Polygon([ pya.Point(1336, 860), pya.Point(1408, 860), pya.Point(1408, 932), pya.Point(1336, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_63)

polygon_N11_64 = pya.Polygon([ pya.Point(1336, -4), pya.Point(1408, -4), pya.Point(1408, 68), pya.Point(1336, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_64)

polygon_N12_65 = pya.Polygon([ pya.Point(1624, 860), pya.Point(1696, 860), pya.Point(1696, 932), pya.Point(1624, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_65)

polygon_N14_66 = pya.Polygon([ pya.Point(1480, 716), pya.Point(1552, 716), pya.Point(1552, 788), pya.Point(1480, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_66)

polygon_N14_67 = pya.Polygon([ pya.Point(1480, 284), pya.Point(1552, 284), pya.Point(1552, 356), pya.Point(1480, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_67)

polygon_N14_68 = pya.Polygon([ pya.Point(1480, -4), pya.Point(1552, -4), pya.Point(1552, 68), pya.Point(1480, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_68)

polygon_N15_69 = pya.Polygon([ pya.Point(184, 428), pya.Point(256, 428), pya.Point(256, 500), pya.Point(184, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N15_69)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1704, -64), pya.Point(1704, 1264), pya.Point(16, 1264)]))

layout.write("../gds/Cell123.gds")
