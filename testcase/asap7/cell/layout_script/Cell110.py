import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell110")

polygon_N1_0 = pya.Polygon([ pya.Point(16, -4), pya.Point(696, -4), pya.Point(696, 68), pya.Point(16, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(16, 716), pya.Point(192, 716), pya.Point(192, 788), pya.Point(16, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N1_2 = pya.Polygon([ pya.Point(16, 1148), pya.Point(336, 1148), pya.Point(336, 1220), pya.Point(16, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_2)

polygon_N1_3 = pya.Polygon([ pya.Point(520, 716), pya.Point(696, 716), pya.Point(696, 788), pya.Point(520, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_3)

polygon_N10_4 = pya.Polygon([ pya.Point(1384, -4), pya.Point(1560, -4), pya.Point(1560, 68), pya.Point(1384, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_4)

polygon_N10_5 = pya.Polygon([ pya.Point(1168, 860), pya.Point(1560, 860), pya.Point(1560, 932), pya.Point(1168, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_5)

polygon_N11_6 = pya.Polygon([ pya.Point(1888, 860), pya.Point(2568, 860), pya.Point(2568, 932), pya.Point(1888, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_6)

polygon_N12_7 = pya.Polygon([ pya.Point(304, 716), pya.Point(480, 716), pya.Point(480, 788), pya.Point(304, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_7)

polygon_N13_8 = pya.Polygon([ pya.Point(1312, 716), pya.Point(1704, 716), pya.Point(1704, 788), pya.Point(1312, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_8)

polygon_N14_9 = pya.Polygon([ pya.Point(880, -4), pya.Point(1056, -4), pya.Point(1056, 68), pya.Point(880, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_9)

polygon_N14_10 = pya.Polygon([ pya.Point(880, 572), pya.Point(2424, 572), pya.Point(2424, 644), pya.Point(880, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_10)

polygon_N14_11 = pya.Polygon([ pya.Point(1816, 716), pya.Point(2640, 716), pya.Point(2640, 788), pya.Point(1816, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_11)

polygon_N14_12 = pya.Polygon([ pya.Point(2320, -4), pya.Point(2496, -4), pya.Point(2496, 68), pya.Point(2320, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_12)

polygon_N14_13 = pya.Polygon([ pya.Point(2032, 284), pya.Point(2712, 284), pya.Point(2712, 356), pya.Point(2032, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_13)

polygon_N15_14 = pya.Polygon([ pya.Point(88, 428), pya.Point(1128, 428), pya.Point(1128, 500), pya.Point(88, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N15_14)

polygon_N16_15 = pya.Polygon([ pya.Point(1168, 428), pya.Point(2496, 428), pya.Point(2496, 500), pya.Point(1168, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N16_15)

polygon_N17_16 = pya.Polygon([ pya.Point(160, 140), pya.Point(840, 140), pya.Point(840, 212), pya.Point(160, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N17_16)

polygon_N18_17 = pya.Polygon([ pya.Point(1816, 140), pya.Point(1992, 140), pya.Point(1992, 212), pya.Point(1816, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N18_17)

polygon_N2_18 = pya.Polygon([ pya.Point(448, 1148), pya.Point(1128, 1148), pya.Point(1128, 1220), pya.Point(448, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_18)

polygon_N3_19 = pya.Polygon([ pya.Point(1168, -4), pya.Point(1344, -4), pya.Point(1344, 68), pya.Point(1168, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_19)

polygon_N3_20 = pya.Polygon([ pya.Point(1096, 716), pya.Point(1272, 716), pya.Point(1272, 788), pya.Point(1096, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_20)

polygon_N3_21 = pya.Polygon([ pya.Point(1168, 1148), pya.Point(1848, 1148), pya.Point(1848, 1220), pya.Point(1168, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_21)

polygon_N3_22 = pya.Polygon([ pya.Point(1600, -4), pya.Point(1848, -4), pya.Point(1848, 68), pya.Point(1600, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_22)

polygon_N4_23 = pya.Polygon([ pya.Point(88, 860), pya.Point(336, 860), pya.Point(336, 932), pya.Point(88, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_23)

polygon_N4_24 = pya.Polygon([ pya.Point(160, 1004), pya.Point(624, 1004), pya.Point(624, 1076), pya.Point(160, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_24)

polygon_N5_25 = pya.Polygon([ pya.Point(736, 716), pya.Point(912, 716), pya.Point(912, 788), pya.Point(736, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_25)

polygon_N5_26 = pya.Polygon([ pya.Point(664, 1004), pya.Point(912, 1004), pya.Point(912, 1076), pya.Point(664, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_26)

polygon_N6_27 = pya.Polygon([ pya.Point(1024, 140), pya.Point(1200, 140), pya.Point(1200, 212), pya.Point(1024, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_27)

polygon_N6_28 = pya.Polygon([ pya.Point(1024, 284), pya.Point(1992, 284), pya.Point(1992, 356), pya.Point(1024, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_28)

polygon_N6_29 = pya.Polygon([ pya.Point(1024, 1004), pya.Point(1200, 1004), pya.Point(1200, 1076), pya.Point(1024, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_29)

polygon_N7_30 = pya.Polygon([ pya.Point(1312, 140), pya.Point(1488, 140), pya.Point(1488, 212), pya.Point(1312, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_30)

polygon_N7_31 = pya.Polygon([ pya.Point(1312, 1004), pya.Point(1488, 1004), pya.Point(1488, 1076), pya.Point(1312, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_31)

polygon_N8_32 = pya.Polygon([ pya.Point(2104, 140), pya.Point(2640, 140), pya.Point(2640, 212), pya.Point(2104, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_32)

polygon_N8_33 = pya.Polygon([ pya.Point(1528, 1004), pya.Point(2568, 1004), pya.Point(2568, 1076), pya.Point(1528, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_33)

polygon_N9_34 = pya.Polygon([ pya.Point(448, 860), pya.Point(1128, 860), pya.Point(1128, 932), pya.Point(448, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_34)

polygon_N1_35 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 832), pya.Point(40, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_35)

polygon_N1_36 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 832), pya.Point(616, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_36)

polygon_N10_37 = pya.Polygon([ pya.Point(1480, -64), pya.Point(1552, -64), pya.Point(1552, 976), pya.Point(1480, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_37)

polygon_N11_38 = pya.Polygon([ pya.Point(2200, 800), pya.Point(2272, 800), pya.Point(2272, 976), pya.Point(2200, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_38)

polygon_N12_39 = pya.Polygon([ pya.Point(328, 656), pya.Point(400, 656), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N12_39)

polygon_N14_40 = pya.Polygon([ pya.Point(904, -64), pya.Point(976, -64), pya.Point(976, 688), pya.Point(904, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N14_40)

polygon_N14_41 = pya.Polygon([ pya.Point(2344, -64), pya.Point(2416, -64), pya.Point(2416, 832), pya.Point(2344, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N14_41)

polygon_N17_42 = pya.Polygon([ pya.Point(328, 80), pya.Point(400, 80), pya.Point(400, 256), pya.Point(328, 256), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N17_42)

polygon_N18_43 = pya.Polygon([ pya.Point(1912, 80), pya.Point(1984, 80), pya.Point(1984, 256), pya.Point(1912, 256), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N18_43)

polygon_N3_44 = pya.Polygon([ pya.Point(1192, -64), pya.Point(1264, -64), pya.Point(1264, 1264), pya.Point(1192, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_44)

polygon_N3_45 = pya.Polygon([ pya.Point(1768, -64), pya.Point(1840, -64), pya.Point(1840, 1264), pya.Point(1768, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_45)

polygon_N4_46 = pya.Polygon([ pya.Point(184, 800), pya.Point(256, 800), pya.Point(256, 1120), pya.Point(184, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_46)

polygon_N5_47 = pya.Polygon([ pya.Point(760, 656), pya.Point(832, 656), pya.Point(832, 832), pya.Point(760, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_47)

polygon_N6_48 = pya.Polygon([ pya.Point(1048, 80), pya.Point(1120, 80), pya.Point(1120, 1120), pya.Point(1048, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_48)

polygon_N7_49 = pya.Polygon([ pya.Point(1336, 80), pya.Point(1408, 80), pya.Point(1408, 1120), pya.Point(1336, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_49)

polygon_N8_50 = pya.Polygon([ pya.Point(2488, 80), pya.Point(2560, 80), pya.Point(2560, 1120), pya.Point(2488, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_50)

polygon_N1_51 = pya.Polygon([ pya.Point(40, 716), pya.Point(112, 716), pya.Point(112, 788), pya.Point(40, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_51)

polygon_N1_52 = pya.Polygon([ pya.Point(616, 716), pya.Point(688, 716), pya.Point(688, 788), pya.Point(616, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_52)

polygon_N1_53 = pya.Polygon([ pya.Point(40, -4), pya.Point(112, -4), pya.Point(112, 68), pya.Point(40, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_53)

polygon_N1_54 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_54)

polygon_N3_55 = pya.Polygon([ pya.Point(1192, 1148), pya.Point(1264, 1148), pya.Point(1264, 1220), pya.Point(1192, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_55)

polygon_N3_56 = pya.Polygon([ pya.Point(1768, 1148), pya.Point(1840, 1148), pya.Point(1840, 1220), pya.Point(1768, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_56)

polygon_N3_57 = pya.Polygon([ pya.Point(1192, 716), pya.Point(1264, 716), pya.Point(1264, 788), pya.Point(1192, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_57)

polygon_N3_58 = pya.Polygon([ pya.Point(1192, -4), pya.Point(1264, -4), pya.Point(1264, 68), pya.Point(1192, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_58)

polygon_N3_59 = pya.Polygon([ pya.Point(1768, -4), pya.Point(1840, -4), pya.Point(1840, 68), pya.Point(1768, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_59)

polygon_N4_60 = pya.Polygon([ pya.Point(184, 1004), pya.Point(256, 1004), pya.Point(256, 1076), pya.Point(184, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_60)

polygon_N4_61 = pya.Polygon([ pya.Point(184, 860), pya.Point(256, 860), pya.Point(256, 932), pya.Point(184, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_61)

polygon_N5_62 = pya.Polygon([ pya.Point(760, 716), pya.Point(832, 716), pya.Point(832, 788), pya.Point(760, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_62)

polygon_N6_63 = pya.Polygon([ pya.Point(1048, 1004), pya.Point(1120, 1004), pya.Point(1120, 1076), pya.Point(1048, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_63)

polygon_N6_64 = pya.Polygon([ pya.Point(1048, 284), pya.Point(1120, 284), pya.Point(1120, 356), pya.Point(1048, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_64)

polygon_N6_65 = pya.Polygon([ pya.Point(1048, 140), pya.Point(1120, 140), pya.Point(1120, 212), pya.Point(1048, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_65)

polygon_N7_66 = pya.Polygon([ pya.Point(1336, 1004), pya.Point(1408, 1004), pya.Point(1408, 1076), pya.Point(1336, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_66)

polygon_N7_67 = pya.Polygon([ pya.Point(1336, 140), pya.Point(1408, 140), pya.Point(1408, 212), pya.Point(1336, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_67)

polygon_N8_68 = pya.Polygon([ pya.Point(2488, 1004), pya.Point(2560, 1004), pya.Point(2560, 1076), pya.Point(2488, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_68)

polygon_N8_69 = pya.Polygon([ pya.Point(2488, 140), pya.Point(2560, 140), pya.Point(2560, 212), pya.Point(2488, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_69)

polygon_N10_70 = pya.Polygon([ pya.Point(1480, 860), pya.Point(1552, 860), pya.Point(1552, 932), pya.Point(1480, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_70)

polygon_N10_71 = pya.Polygon([ pya.Point(1480, -4), pya.Point(1552, -4), pya.Point(1552, 68), pya.Point(1480, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_71)

polygon_N11_72 = pya.Polygon([ pya.Point(2200, 860), pya.Point(2272, 860), pya.Point(2272, 932), pya.Point(2200, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_72)

polygon_N12_73 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_73)

polygon_N14_74 = pya.Polygon([ pya.Point(2344, 716), pya.Point(2416, 716), pya.Point(2416, 788), pya.Point(2344, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_74)

polygon_N14_75 = pya.Polygon([ pya.Point(904, 572), pya.Point(976, 572), pya.Point(976, 644), pya.Point(904, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_75)

polygon_N14_76 = pya.Polygon([ pya.Point(2344, 572), pya.Point(2416, 572), pya.Point(2416, 644), pya.Point(2344, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_76)

polygon_N14_77 = pya.Polygon([ pya.Point(2344, 284), pya.Point(2416, 284), pya.Point(2416, 356), pya.Point(2344, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_77)

polygon_N14_78 = pya.Polygon([ pya.Point(904, -4), pya.Point(976, -4), pya.Point(976, 68), pya.Point(904, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_78)

polygon_N14_79 = pya.Polygon([ pya.Point(2344, -4), pya.Point(2416, -4), pya.Point(2416, 68), pya.Point(2344, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_79)

polygon_N17_80 = pya.Polygon([ pya.Point(328, 140), pya.Point(400, 140), pya.Point(400, 212), pya.Point(328, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N17_80)

polygon_N18_81 = pya.Polygon([ pya.Point(1912, 140), pya.Point(1984, 140), pya.Point(1984, 212), pya.Point(1912, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N18_81)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(2712, -64), pya.Point(2712, 1264), pya.Point(16, 1264)]))

layout.write("../gds/Cell110.gds")
