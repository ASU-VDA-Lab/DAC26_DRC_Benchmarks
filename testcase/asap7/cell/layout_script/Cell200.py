import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell200")

polygon_N1_0 = pya.Polygon([ pya.Point(448, 1004), pya.Point(840, 1004), pya.Point(840, 1076), pya.Point(448, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(16, 1148), pya.Point(552, 1148), pya.Point(552, 1220), pya.Point(16, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N10_2 = pya.Polygon([ pya.Point(376, 716), pya.Point(624, 716), pya.Point(624, 788), pya.Point(376, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_2)

polygon_N11_3 = pya.Polygon([ pya.Point(880, 716), pya.Point(1632, 716), pya.Point(1632, 788), pya.Point(880, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_3)

polygon_N12_4 = pya.Polygon([ pya.Point(880, 428), pya.Point(1632, 428), pya.Point(1632, 500), pya.Point(880, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_4)

polygon_N12_5 = pya.Polygon([ pya.Point(1528, 140), pya.Point(1920, 140), pya.Point(1920, 212), pya.Point(1528, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_5)

polygon_N12_6 = pya.Polygon([ pya.Point(1672, 716), pya.Point(1920, 716), pya.Point(1920, 788), pya.Point(1672, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_6)

polygon_N13_7 = pya.Polygon([ pya.Point(664, 140), pya.Point(984, 140), pya.Point(984, 212), pya.Point(664, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_7)

polygon_N13_8 = pya.Polygon([ pya.Point(880, 572), pya.Point(1992, 572), pya.Point(1992, 644), pya.Point(880, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_8)

polygon_N13_9 = pya.Polygon([ pya.Point(1816, -4), pya.Point(1992, -4), pya.Point(1992, 68), pya.Point(1816, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_9)

polygon_N14_10 = pya.Polygon([ pya.Point(448, 140), pya.Point(624, 140), pya.Point(624, 212), pya.Point(448, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_10)

polygon_N2_11 = pya.Polygon([ pya.Point(16, -4), pya.Point(696, -4), pya.Point(696, 68), pya.Point(16, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_11)

polygon_N2_12 = pya.Polygon([ pya.Point(16, 716), pya.Point(336, 716), pya.Point(336, 788), pya.Point(16, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_12)

polygon_N2_13 = pya.Polygon([ pya.Point(592, 1148), pya.Point(768, 1148), pya.Point(768, 1220), pya.Point(592, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_13)

polygon_N3_14 = pya.Polygon([ pya.Point(736, -4), pya.Point(912, -4), pya.Point(912, 68), pya.Point(736, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_14)

polygon_N3_15 = pya.Polygon([ pya.Point(448, 284), pya.Point(1488, 284), pya.Point(1488, 356), pya.Point(448, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_15)

polygon_N3_16 = pya.Polygon([ pya.Point(808, 1148), pya.Point(1128, 1148), pya.Point(1128, 1220), pya.Point(808, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_16)

polygon_N4_17 = pya.Polygon([ pya.Point(16, 1004), pya.Point(192, 1004), pya.Point(192, 1076), pya.Point(16, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_17)

polygon_N5_18 = pya.Polygon([ pya.Point(232, 140), pya.Point(408, 140), pya.Point(408, 212), pya.Point(232, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_18)

polygon_N5_19 = pya.Polygon([ pya.Point(304, 860), pya.Point(768, 860), pya.Point(768, 932), pya.Point(304, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_19)

polygon_N5_20 = pya.Polygon([ pya.Point(232, 1004), pya.Point(408, 1004), pya.Point(408, 1076), pya.Point(232, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_20)

polygon_N6_21 = pya.Polygon([ pya.Point(952, -4), pya.Point(1560, -4), pya.Point(1560, 68), pya.Point(952, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_21)

polygon_N6_22 = pya.Polygon([ pya.Point(808, 860), pya.Point(984, 860), pya.Point(984, 932), pya.Point(808, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_22)

polygon_N6_23 = pya.Polygon([ pya.Point(880, 1004), pya.Point(1560, 1004), pya.Point(1560, 1076), pya.Point(880, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_23)

polygon_N7_24 = pya.Polygon([ pya.Point(160, 572), pya.Point(840, 572), pya.Point(840, 644), pya.Point(160, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_24)

polygon_N7_25 = pya.Polygon([ pya.Point(16, 860), pya.Point(264, 860), pya.Point(264, 932), pya.Point(16, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_25)

polygon_N7_26 = pya.Polygon([ pya.Point(664, 716), pya.Point(840, 716), pya.Point(840, 788), pya.Point(664, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_26)

polygon_N8_27 = pya.Polygon([ pya.Point(1024, 140), pya.Point(1272, 140), pya.Point(1272, 212), pya.Point(1024, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_27)

polygon_N8_28 = pya.Polygon([ pya.Point(1096, 860), pya.Point(1560, 860), pya.Point(1560, 932), pya.Point(1096, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_28)

polygon_N9_29 = pya.Polygon([ pya.Point(1600, -4), pya.Point(1776, -4), pya.Point(1776, 68), pya.Point(1600, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_29)

polygon_N9_30 = pya.Polygon([ pya.Point(1600, 860), pya.Point(1848, 860), pya.Point(1848, 932), pya.Point(1600, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_30)

polygon_N1_31 = pya.Polygon([ pya.Point(472, 944), pya.Point(544, 944), pya.Point(544, 1264), pya.Point(472, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_31)

polygon_N10_32 = pya.Polygon([ pya.Point(472, 656), pya.Point(544, 656), pya.Point(544, 832), pya.Point(472, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_32)

polygon_N12_33 = pya.Polygon([ pya.Point(1768, 80), pya.Point(1840, 80), pya.Point(1840, 832), pya.Point(1768, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N12_33)

polygon_N13_34 = pya.Polygon([ pya.Point(1912, -64), pya.Point(1984, -64), pya.Point(1984, 688), pya.Point(1912, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N13_34)

polygon_N13_35 = pya.Polygon([ pya.Point(904, 80), pya.Point(976, 80), pya.Point(976, 688), pya.Point(904, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N13_35)

polygon_N14_36 = pya.Polygon([ pya.Point(472, 80), pya.Point(544, 80), pya.Point(544, 256), pya.Point(472, 256), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N14_36)

polygon_N2_37 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 832), pya.Point(40, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_37)

polygon_N2_38 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 1264), pya.Point(616, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_38)

polygon_N3_39 = pya.Polygon([ pya.Point(760, -64), pya.Point(832, -64), pya.Point(832, 400), pya.Point(760, 400), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_39)

polygon_N3_40 = pya.Polygon([ pya.Point(1048, 224), pya.Point(1120, 224), pya.Point(1120, 1264), pya.Point(1048, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_40)

polygon_N4_41 = pya.Polygon([ pya.Point(40, 944), pya.Point(112, 944), pya.Point(112, 1120), pya.Point(40, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_41)

polygon_N5_42 = pya.Polygon([ pya.Point(328, 80), pya.Point(400, 80), pya.Point(400, 1120), pya.Point(328, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_42)

polygon_N6_43 = pya.Polygon([ pya.Point(1480, -64), pya.Point(1552, -64), pya.Point(1552, 1120), pya.Point(1480, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_43)

polygon_N6_44 = pya.Polygon([ pya.Point(904, 800), pya.Point(976, 800), pya.Point(976, 1120), pya.Point(904, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_44)

polygon_N7_45 = pya.Polygon([ pya.Point(184, 512), pya.Point(256, 512), pya.Point(256, 976), pya.Point(184, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_45)

polygon_N7_46 = pya.Polygon([ pya.Point(760, 512), pya.Point(832, 512), pya.Point(832, 832), pya.Point(760, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_46)

polygon_N8_47 = pya.Polygon([ pya.Point(1192, 80), pya.Point(1264, 80), pya.Point(1264, 976), pya.Point(1192, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_47)

polygon_N9_48 = pya.Polygon([ pya.Point(1624, -64), pya.Point(1696, -64), pya.Point(1696, 976), pya.Point(1624, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_48)

polygon_N1_49 = pya.Polygon([ pya.Point(472, 1148), pya.Point(544, 1148), pya.Point(544, 1220), pya.Point(472, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_49)

polygon_N1_50 = pya.Polygon([ pya.Point(472, 1004), pya.Point(544, 1004), pya.Point(544, 1076), pya.Point(472, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_50)

polygon_N2_51 = pya.Polygon([ pya.Point(616, 1148), pya.Point(688, 1148), pya.Point(688, 1220), pya.Point(616, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_51)

polygon_N2_52 = pya.Polygon([ pya.Point(40, 716), pya.Point(112, 716), pya.Point(112, 788), pya.Point(40, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_52)

polygon_N2_53 = pya.Polygon([ pya.Point(40, -4), pya.Point(112, -4), pya.Point(112, 68), pya.Point(40, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_53)

polygon_N2_54 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_54)

polygon_N3_55 = pya.Polygon([ pya.Point(1048, 1148), pya.Point(1120, 1148), pya.Point(1120, 1220), pya.Point(1048, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_55)

polygon_N3_56 = pya.Polygon([ pya.Point(760, 284), pya.Point(832, 284), pya.Point(832, 356), pya.Point(760, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_56)

polygon_N3_57 = pya.Polygon([ pya.Point(1048, 284), pya.Point(1120, 284), pya.Point(1120, 356), pya.Point(1048, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_57)

polygon_N3_58 = pya.Polygon([ pya.Point(760, -4), pya.Point(832, -4), pya.Point(832, 68), pya.Point(760, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_58)

polygon_N4_59 = pya.Polygon([ pya.Point(40, 1004), pya.Point(112, 1004), pya.Point(112, 1076), pya.Point(40, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_59)

polygon_N5_60 = pya.Polygon([ pya.Point(328, 1004), pya.Point(400, 1004), pya.Point(400, 1076), pya.Point(328, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_60)

polygon_N5_61 = pya.Polygon([ pya.Point(328, 860), pya.Point(400, 860), pya.Point(400, 932), pya.Point(328, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_61)

polygon_N5_62 = pya.Polygon([ pya.Point(328, 140), pya.Point(400, 140), pya.Point(400, 212), pya.Point(328, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_62)

polygon_N6_63 = pya.Polygon([ pya.Point(904, 1004), pya.Point(976, 1004), pya.Point(976, 1076), pya.Point(904, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_63)

polygon_N6_64 = pya.Polygon([ pya.Point(1480, 1004), pya.Point(1552, 1004), pya.Point(1552, 1076), pya.Point(1480, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_64)

polygon_N6_65 = pya.Polygon([ pya.Point(904, 860), pya.Point(976, 860), pya.Point(976, 932), pya.Point(904, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_65)

polygon_N6_66 = pya.Polygon([ pya.Point(1480, -4), pya.Point(1552, -4), pya.Point(1552, 68), pya.Point(1480, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_66)

polygon_N7_67 = pya.Polygon([ pya.Point(184, 860), pya.Point(256, 860), pya.Point(256, 932), pya.Point(184, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_67)

polygon_N7_68 = pya.Polygon([ pya.Point(760, 716), pya.Point(832, 716), pya.Point(832, 788), pya.Point(760, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_68)

polygon_N7_69 = pya.Polygon([ pya.Point(184, 572), pya.Point(256, 572), pya.Point(256, 644), pya.Point(184, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_69)

polygon_N7_70 = pya.Polygon([ pya.Point(760, 572), pya.Point(832, 572), pya.Point(832, 644), pya.Point(760, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_70)

polygon_N8_71 = pya.Polygon([ pya.Point(1192, 860), pya.Point(1264, 860), pya.Point(1264, 932), pya.Point(1192, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_71)

polygon_N8_72 = pya.Polygon([ pya.Point(1192, 140), pya.Point(1264, 140), pya.Point(1264, 212), pya.Point(1192, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_72)

polygon_N9_73 = pya.Polygon([ pya.Point(1624, 860), pya.Point(1696, 860), pya.Point(1696, 932), pya.Point(1624, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_73)

polygon_N9_74 = pya.Polygon([ pya.Point(1624, -4), pya.Point(1696, -4), pya.Point(1696, 68), pya.Point(1624, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_74)

polygon_N10_75 = pya.Polygon([ pya.Point(472, 716), pya.Point(544, 716), pya.Point(544, 788), pya.Point(472, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_75)

polygon_N12_76 = pya.Polygon([ pya.Point(1768, 716), pya.Point(1840, 716), pya.Point(1840, 788), pya.Point(1768, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_76)

polygon_N12_77 = pya.Polygon([ pya.Point(1768, 140), pya.Point(1840, 140), pya.Point(1840, 212), pya.Point(1768, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_77)

polygon_N13_78 = pya.Polygon([ pya.Point(904, 572), pya.Point(976, 572), pya.Point(976, 644), pya.Point(904, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_78)

polygon_N13_79 = pya.Polygon([ pya.Point(1912, 572), pya.Point(1984, 572), pya.Point(1984, 644), pya.Point(1912, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_79)

polygon_N13_80 = pya.Polygon([ pya.Point(904, 140), pya.Point(976, 140), pya.Point(976, 212), pya.Point(904, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_80)

polygon_N13_81 = pya.Polygon([ pya.Point(1912, -4), pya.Point(1984, -4), pya.Point(1984, 68), pya.Point(1912, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_81)

polygon_N14_82 = pya.Polygon([ pya.Point(472, 140), pya.Point(544, 140), pya.Point(544, 212), pya.Point(472, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_82)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1992, -64), pya.Point(1992, 1264), pya.Point(16, 1264)]))

layout.write("../gds/Cell200.gds")
