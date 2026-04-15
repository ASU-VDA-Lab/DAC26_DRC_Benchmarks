import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell112")

polygon_N1_0 = pya.Polygon([ pya.Point(16, 140), pya.Point(696, 140), pya.Point(696, 212), pya.Point(16, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(16, 716), pya.Point(264, 716), pya.Point(264, 788), pya.Point(16, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N1_2 = pya.Polygon([ pya.Point(16, 1148), pya.Point(336, 1148), pya.Point(336, 1220), pya.Point(16, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_2)

polygon_N1_3 = pya.Polygon([ pya.Point(520, 716), pya.Point(696, 716), pya.Point(696, 788), pya.Point(520, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_3)

polygon_N10_4 = pya.Polygon([ pya.Point(1384, -4), pya.Point(1560, -4), pya.Point(1560, 68), pya.Point(1384, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_4)

polygon_N10_5 = pya.Polygon([ pya.Point(1168, 860), pya.Point(1560, 860), pya.Point(1560, 932), pya.Point(1168, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_5)

polygon_N11_6 = pya.Polygon([ pya.Point(952, 428), pya.Point(2712, 428), pya.Point(2712, 500), pya.Point(952, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_6)

polygon_N11_7 = pya.Polygon([ pya.Point(1816, 860), pya.Point(2640, 860), pya.Point(2640, 932), pya.Point(1816, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_7)

polygon_N11_8 = pya.Polygon([ pya.Point(2320, -4), pya.Point(2568, -4), pya.Point(2568, 68), pya.Point(2320, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_8)

polygon_N12_9 = pya.Polygon([ pya.Point(304, 716), pya.Point(480, 716), pya.Point(480, 788), pya.Point(304, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_9)

polygon_N13_10 = pya.Polygon([ pya.Point(1240, 140), pya.Point(1416, 140), pya.Point(1416, 212), pya.Point(1240, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_10)

polygon_N13_11 = pya.Polygon([ pya.Point(1312, 716), pya.Point(1488, 716), pya.Point(1488, 788), pya.Point(1312, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_11)

polygon_N14_12 = pya.Polygon([ pya.Point(1528, 716), pya.Point(2280, 716), pya.Point(2280, 788), pya.Point(1528, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_12)

polygon_N14_13 = pya.Polygon([ pya.Point(2104, 140), pya.Point(2640, 140), pya.Point(2640, 212), pya.Point(2104, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_13)

polygon_N15_14 = pya.Polygon([ pya.Point(88, -4), pya.Point(336, -4), pya.Point(336, 68), pya.Point(88, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N15_14)

polygon_N15_15 = pya.Polygon([ pya.Point(160, 428), pya.Point(840, 428), pya.Point(840, 500), pya.Point(160, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N15_15)

polygon_N16_16 = pya.Polygon([ pya.Point(88, 284), pya.Point(1128, 284), pya.Point(1128, 356), pya.Point(88, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N16_16)

polygon_N17_17 = pya.Polygon([ pya.Point(1168, 284), pya.Point(2496, 284), pya.Point(2496, 356), pya.Point(1168, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N17_17)

polygon_N18_18 = pya.Polygon([ pya.Point(1816, -4), pya.Point(2136, -4), pya.Point(2136, 68), pya.Point(1816, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N18_18)

polygon_N2_19 = pya.Polygon([ pya.Point(448, 1148), pya.Point(1128, 1148), pya.Point(1128, 1220), pya.Point(448, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_19)

polygon_N3_20 = pya.Polygon([ pya.Point(1168, -4), pya.Point(1344, -4), pya.Point(1344, 68), pya.Point(1168, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_20)

polygon_N3_21 = pya.Polygon([ pya.Point(1096, 716), pya.Point(1272, 716), pya.Point(1272, 788), pya.Point(1096, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_21)

polygon_N3_22 = pya.Polygon([ pya.Point(1168, 1148), pya.Point(1848, 1148), pya.Point(1848, 1220), pya.Point(1168, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_22)

polygon_N3_23 = pya.Polygon([ pya.Point(1600, 140), pya.Point(1848, 140), pya.Point(1848, 212), pya.Point(1600, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_23)

polygon_N4_24 = pya.Polygon([ pya.Point(88, 860), pya.Point(336, 860), pya.Point(336, 932), pya.Point(88, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_24)

polygon_N4_25 = pya.Polygon([ pya.Point(160, 1004), pya.Point(624, 1004), pya.Point(624, 1076), pya.Point(160, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_25)

polygon_N5_26 = pya.Polygon([ pya.Point(880, 140), pya.Point(1200, 140), pya.Point(1200, 212), pya.Point(880, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_26)

polygon_N5_27 = pya.Polygon([ pya.Point(880, 572), pya.Point(1992, 572), pya.Point(1992, 644), pya.Point(880, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_27)

polygon_N5_28 = pya.Polygon([ pya.Point(880, 1004), pya.Point(1200, 1004), pya.Point(1200, 1076), pya.Point(880, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_28)

polygon_N5_29 = pya.Polygon([ pya.Point(1600, -4), pya.Point(1776, -4), pya.Point(1776, 68), pya.Point(1600, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_29)

polygon_N5_30 = pya.Polygon([ pya.Point(1888, 140), pya.Point(2064, 140), pya.Point(2064, 212), pya.Point(1888, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_30)

polygon_N6_31 = pya.Polygon([ pya.Point(1600, 860), pya.Point(1776, 860), pya.Point(1776, 932), pya.Point(1600, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_31)

polygon_N6_32 = pya.Polygon([ pya.Point(1312, 1004), pya.Point(1704, 1004), pya.Point(1704, 1076), pya.Point(1312, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_32)

polygon_N7_33 = pya.Polygon([ pya.Point(2464, 716), pya.Point(2712, 716), pya.Point(2712, 788), pya.Point(2464, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_33)

polygon_N7_34 = pya.Polygon([ pya.Point(1888, 1004), pya.Point(2568, 1004), pya.Point(2568, 1076), pya.Point(1888, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_34)

polygon_N8_35 = pya.Polygon([ pya.Point(448, -4), pya.Point(1128, -4), pya.Point(1128, 68), pya.Point(448, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_35)

polygon_N8_36 = pya.Polygon([ pya.Point(376, 860), pya.Point(552, 860), pya.Point(552, 932), pya.Point(376, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_36)

polygon_N8_37 = pya.Polygon([ pya.Point(952, 860), pya.Point(1128, 860), pya.Point(1128, 932), pya.Point(952, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_37)

polygon_N9_38 = pya.Polygon([ pya.Point(664, 860), pya.Point(912, 860), pya.Point(912, 932), pya.Point(664, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_38)

polygon_N1_39 = pya.Polygon([ pya.Point(40, 80), pya.Point(112, 80), pya.Point(112, 832), pya.Point(40, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_39)

polygon_N1_40 = pya.Polygon([ pya.Point(616, 80), pya.Point(688, 80), pya.Point(688, 832), pya.Point(616, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_40)

polygon_N10_41 = pya.Polygon([ pya.Point(1480, -64), pya.Point(1552, -64), pya.Point(1552, 976), pya.Point(1480, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_41)

polygon_N11_42 = pya.Polygon([ pya.Point(2488, -64), pya.Point(2560, -64), pya.Point(2560, 976), pya.Point(2488, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_42)

polygon_N12_43 = pya.Polygon([ pya.Point(328, 656), pya.Point(400, 656), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N12_43)

polygon_N13_44 = pya.Polygon([ pya.Point(1336, 80), pya.Point(1408, 80), pya.Point(1408, 832), pya.Point(1336, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N13_44)

polygon_N14_45 = pya.Polygon([ pya.Point(2200, 80), pya.Point(2272, 80), pya.Point(2272, 832), pya.Point(2200, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N14_45)

polygon_N15_46 = pya.Polygon([ pya.Point(184, -64), pya.Point(256, -64), pya.Point(256, 112), pya.Point(184, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N15_46)

polygon_N18_47 = pya.Polygon([ pya.Point(2056, -64), pya.Point(2128, -64), pya.Point(2128, 112), pya.Point(2056, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N18_47)

polygon_N3_48 = pya.Polygon([ pya.Point(1192, -64), pya.Point(1264, -64), pya.Point(1264, 1264), pya.Point(1192, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_48)

polygon_N3_49 = pya.Polygon([ pya.Point(1768, 80), pya.Point(1840, 80), pya.Point(1840, 1264), pya.Point(1768, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_49)

polygon_N4_50 = pya.Polygon([ pya.Point(184, 800), pya.Point(256, 800), pya.Point(256, 1120), pya.Point(184, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_50)

polygon_N5_51 = pya.Polygon([ pya.Point(904, 80), pya.Point(976, 80), pya.Point(976, 1120), pya.Point(904, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_51)

polygon_N5_52 = pya.Polygon([ pya.Point(1624, -64), pya.Point(1696, -64), pya.Point(1696, 688), pya.Point(1624, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_52)

polygon_N5_53 = pya.Polygon([ pya.Point(1912, 80), pya.Point(1984, 80), pya.Point(1984, 688), pya.Point(1912, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_53)

polygon_N6_54 = pya.Polygon([ pya.Point(1624, 800), pya.Point(1696, 800), pya.Point(1696, 1120), pya.Point(1624, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_54)

polygon_N7_55 = pya.Polygon([ pya.Point(2632, 656), pya.Point(2704, 656), pya.Point(2704, 832), pya.Point(2632, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_55)

polygon_N8_56 = pya.Polygon([ pya.Point(472, -64), pya.Point(544, -64), pya.Point(544, 976), pya.Point(472, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_56)

polygon_N8_57 = pya.Polygon([ pya.Point(1048, -64), pya.Point(1120, -64), pya.Point(1120, 976), pya.Point(1048, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_57)

polygon_N9_58 = pya.Polygon([ pya.Point(760, 800), pya.Point(832, 800), pya.Point(832, 976), pya.Point(760, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_58)

polygon_N1_59 = pya.Polygon([ pya.Point(40, 716), pya.Point(112, 716), pya.Point(112, 788), pya.Point(40, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_59)

polygon_N1_60 = pya.Polygon([ pya.Point(616, 716), pya.Point(688, 716), pya.Point(688, 788), pya.Point(616, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_60)

polygon_N1_61 = pya.Polygon([ pya.Point(40, 140), pya.Point(112, 140), pya.Point(112, 212), pya.Point(40, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_61)

polygon_N1_62 = pya.Polygon([ pya.Point(616, 140), pya.Point(688, 140), pya.Point(688, 212), pya.Point(616, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_62)

polygon_N3_63 = pya.Polygon([ pya.Point(1192, 1148), pya.Point(1264, 1148), pya.Point(1264, 1220), pya.Point(1192, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_63)

polygon_N3_64 = pya.Polygon([ pya.Point(1768, 1148), pya.Point(1840, 1148), pya.Point(1840, 1220), pya.Point(1768, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_64)

polygon_N3_65 = pya.Polygon([ pya.Point(1192, 716), pya.Point(1264, 716), pya.Point(1264, 788), pya.Point(1192, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_65)

polygon_N3_66 = pya.Polygon([ pya.Point(1768, 140), pya.Point(1840, 140), pya.Point(1840, 212), pya.Point(1768, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_66)

polygon_N3_67 = pya.Polygon([ pya.Point(1192, -4), pya.Point(1264, -4), pya.Point(1264, 68), pya.Point(1192, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_67)

polygon_N4_68 = pya.Polygon([ pya.Point(184, 1004), pya.Point(256, 1004), pya.Point(256, 1076), pya.Point(184, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_68)

polygon_N4_69 = pya.Polygon([ pya.Point(184, 860), pya.Point(256, 860), pya.Point(256, 932), pya.Point(184, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_69)

polygon_N5_70 = pya.Polygon([ pya.Point(904, 1004), pya.Point(976, 1004), pya.Point(976, 1076), pya.Point(904, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_70)

polygon_N5_71 = pya.Polygon([ pya.Point(904, 572), pya.Point(976, 572), pya.Point(976, 644), pya.Point(904, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_71)

polygon_N5_72 = pya.Polygon([ pya.Point(1624, 572), pya.Point(1696, 572), pya.Point(1696, 644), pya.Point(1624, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_72)

polygon_N5_73 = pya.Polygon([ pya.Point(1912, 572), pya.Point(1984, 572), pya.Point(1984, 644), pya.Point(1912, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_73)

polygon_N5_74 = pya.Polygon([ pya.Point(904, 140), pya.Point(976, 140), pya.Point(976, 212), pya.Point(904, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_74)

polygon_N5_75 = pya.Polygon([ pya.Point(1912, 140), pya.Point(1984, 140), pya.Point(1984, 212), pya.Point(1912, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_75)

polygon_N5_76 = pya.Polygon([ pya.Point(1624, -4), pya.Point(1696, -4), pya.Point(1696, 68), pya.Point(1624, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_76)

polygon_N6_77 = pya.Polygon([ pya.Point(1624, 1004), pya.Point(1696, 1004), pya.Point(1696, 1076), pya.Point(1624, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_77)

polygon_N6_78 = pya.Polygon([ pya.Point(1624, 860), pya.Point(1696, 860), pya.Point(1696, 932), pya.Point(1624, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_78)

polygon_N7_79 = pya.Polygon([ pya.Point(2632, 716), pya.Point(2704, 716), pya.Point(2704, 788), pya.Point(2632, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_79)

polygon_N8_80 = pya.Polygon([ pya.Point(472, 860), pya.Point(544, 860), pya.Point(544, 932), pya.Point(472, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_80)

polygon_N8_81 = pya.Polygon([ pya.Point(1048, 860), pya.Point(1120, 860), pya.Point(1120, 932), pya.Point(1048, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_81)

polygon_N8_82 = pya.Polygon([ pya.Point(472, -4), pya.Point(544, -4), pya.Point(544, 68), pya.Point(472, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_82)

polygon_N8_83 = pya.Polygon([ pya.Point(1048, -4), pya.Point(1120, -4), pya.Point(1120, 68), pya.Point(1048, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_83)

polygon_N9_84 = pya.Polygon([ pya.Point(760, 860), pya.Point(832, 860), pya.Point(832, 932), pya.Point(760, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_84)

polygon_N10_85 = pya.Polygon([ pya.Point(1480, 860), pya.Point(1552, 860), pya.Point(1552, 932), pya.Point(1480, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_85)

polygon_N10_86 = pya.Polygon([ pya.Point(1480, -4), pya.Point(1552, -4), pya.Point(1552, 68), pya.Point(1480, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_86)

polygon_N11_87 = pya.Polygon([ pya.Point(2488, 860), pya.Point(2560, 860), pya.Point(2560, 932), pya.Point(2488, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_87)

polygon_N11_88 = pya.Polygon([ pya.Point(2488, 428), pya.Point(2560, 428), pya.Point(2560, 500), pya.Point(2488, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_88)

polygon_N11_89 = pya.Polygon([ pya.Point(2488, -4), pya.Point(2560, -4), pya.Point(2560, 68), pya.Point(2488, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_89)

polygon_N12_90 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_90)

polygon_N13_91 = pya.Polygon([ pya.Point(1336, 716), pya.Point(1408, 716), pya.Point(1408, 788), pya.Point(1336, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_91)

polygon_N13_92 = pya.Polygon([ pya.Point(1336, 140), pya.Point(1408, 140), pya.Point(1408, 212), pya.Point(1336, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_92)

polygon_N14_93 = pya.Polygon([ pya.Point(2200, 716), pya.Point(2272, 716), pya.Point(2272, 788), pya.Point(2200, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_93)

polygon_N14_94 = pya.Polygon([ pya.Point(2200, 140), pya.Point(2272, 140), pya.Point(2272, 212), pya.Point(2200, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_94)

polygon_N15_95 = pya.Polygon([ pya.Point(184, -4), pya.Point(256, -4), pya.Point(256, 68), pya.Point(184, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N15_95)

polygon_N18_96 = pya.Polygon([ pya.Point(2056, -4), pya.Point(2128, -4), pya.Point(2128, 68), pya.Point(2056, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N18_96)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(2712, -64), pya.Point(2712, 1264), pya.Point(16, 1264)]))

layout.write("../gds/Cell112.gds")
