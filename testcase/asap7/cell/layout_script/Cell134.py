import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell134")

polygon_N1_0 = pya.Polygon([ pya.Point(304, 1148), pya.Point(1416, 1148), pya.Point(1416, 1220), pya.Point(304, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N10_1 = pya.Polygon([ pya.Point(880, 284), pya.Point(1128, 284), pya.Point(1128, 356), pya.Point(880, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_1)

polygon_N10_2 = pya.Polygon([ pya.Point(880, 716), pya.Point(1056, 716), pya.Point(1056, 788), pya.Point(880, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_2)

polygon_N11_3 = pya.Polygon([ pya.Point(952, 140), pya.Point(1272, 140), pya.Point(1272, 212), pya.Point(952, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_3)

polygon_N11_4 = pya.Polygon([ pya.Point(1096, 716), pya.Point(1272, 716), pya.Point(1272, 788), pya.Point(1096, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_4)

polygon_N12_5 = pya.Polygon([ pya.Point(1384, 716), pya.Point(1560, 716), pya.Point(1560, 788), pya.Point(1384, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_5)

polygon_N13_6 = pya.Polygon([ pya.Point(1672, -4), pya.Point(1848, -4), pya.Point(1848, 68), pya.Point(1672, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_6)

polygon_N13_7 = pya.Polygon([ pya.Point(1384, 428), pya.Point(1848, 428), pya.Point(1848, 500), pya.Point(1384, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_7)

polygon_N13_8 = pya.Polygon([ pya.Point(1672, 716), pya.Point(1848, 716), pya.Point(1848, 788), pya.Point(1672, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_8)

polygon_N14_9 = pya.Polygon([ pya.Point(1168, 284), pya.Point(1776, 284), pya.Point(1776, 356), pya.Point(1168, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_9)

polygon_N15_10 = pya.Polygon([ pya.Point(664, 140), pya.Point(840, 140), pya.Point(840, 212), pya.Point(664, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N15_10)

polygon_N2_11 = pya.Polygon([ pya.Point(16, -4), pya.Point(408, -4), pya.Point(408, 68), pya.Point(16, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_11)

polygon_N2_12 = pya.Polygon([ pya.Point(304, 716), pya.Point(480, 716), pya.Point(480, 788), pya.Point(304, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_12)

polygon_N2_13 = pya.Polygon([ pya.Point(16, 1004), pya.Point(192, 1004), pya.Point(192, 1076), pya.Point(16, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_13)

polygon_N3_14 = pya.Polygon([ pya.Point(88, 140), pya.Point(552, 140), pya.Point(552, 212), pya.Point(88, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_14)

polygon_N3_15 = pya.Polygon([ pya.Point(88, 716), pya.Point(264, 716), pya.Point(264, 788), pya.Point(88, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_15)

polygon_N3_16 = pya.Polygon([ pya.Point(376, 1004), pya.Point(552, 1004), pya.Point(552, 1076), pya.Point(376, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_16)

polygon_N4_17 = pya.Polygon([ pya.Point(736, -4), pya.Point(1200, -4), pya.Point(1200, 68), pya.Point(736, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_17)

polygon_N4_18 = pya.Polygon([ pya.Point(520, 284), pya.Point(840, 284), pya.Point(840, 356), pya.Point(520, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_18)

polygon_N4_19 = pya.Polygon([ pya.Point(1024, 428), pya.Point(1344, 428), pya.Point(1344, 500), pya.Point(1024, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_19)

polygon_N4_20 = pya.Polygon([ pya.Point(1024, 1004), pya.Point(1200, 1004), pya.Point(1200, 1076), pya.Point(1024, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_20)

polygon_N5_21 = pya.Polygon([ pya.Point(448, -4), pya.Point(696, -4), pya.Point(696, 68), pya.Point(448, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_21)

polygon_N5_22 = pya.Polygon([ pya.Point(592, 572), pya.Point(1416, 572), pya.Point(1416, 644), pya.Point(592, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_22)

polygon_N5_23 = pya.Polygon([ pya.Point(1240, -4), pya.Point(1416, -4), pya.Point(1416, 68), pya.Point(1240, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_23)

polygon_N5_24 = pya.Polygon([ pya.Point(1240, 1004), pya.Point(1416, 1004), pya.Point(1416, 1076), pya.Point(1240, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_24)

polygon_N6_25 = pya.Polygon([ pya.Point(1672, 1004), pya.Point(1848, 1004), pya.Point(1848, 1076), pya.Point(1672, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_25)

polygon_N7_26 = pya.Polygon([ pya.Point(232, 860), pya.Point(696, 860), pya.Point(696, 932), pya.Point(232, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_26)

polygon_N8_27 = pya.Polygon([ pya.Point(1312, 140), pya.Point(1704, 140), pya.Point(1704, 212), pya.Point(1312, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_27)

polygon_N8_28 = pya.Polygon([ pya.Point(1528, 860), pya.Point(1704, 860), pya.Point(1704, 932), pya.Point(1528, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_28)

polygon_N9_29 = pya.Polygon([ pya.Point(520, 716), pya.Point(840, 716), pya.Point(840, 788), pya.Point(520, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_29)

polygon_N10_30 = pya.Polygon([ pya.Point(904, 224), pya.Point(976, 224), pya.Point(976, 832), pya.Point(904, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_30)

polygon_N11_31 = pya.Polygon([ pya.Point(1192, 80), pya.Point(1264, 80), pya.Point(1264, 832), pya.Point(1192, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_31)

polygon_N12_32 = pya.Polygon([ pya.Point(1480, 656), pya.Point(1552, 656), pya.Point(1552, 832), pya.Point(1480, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N12_32)

polygon_N13_33 = pya.Polygon([ pya.Point(1768, -64), pya.Point(1840, -64), pya.Point(1840, 832), pya.Point(1768, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N13_33)

polygon_N15_34 = pya.Polygon([ pya.Point(760, 80), pya.Point(832, 80), pya.Point(832, 256), pya.Point(760, 256), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N15_34)

polygon_N2_35 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 1120), pya.Point(40, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_35)

polygon_N2_36 = pya.Polygon([ pya.Point(328, -64), pya.Point(400, -64), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_36)

polygon_N3_37 = pya.Polygon([ pya.Point(184, 80), pya.Point(256, 80), pya.Point(256, 832), pya.Point(184, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_37)

polygon_N3_38 = pya.Polygon([ pya.Point(472, 80), pya.Point(544, 80), pya.Point(544, 1120), pya.Point(472, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_38)

polygon_N4_39 = pya.Polygon([ pya.Point(1048, -64), pya.Point(1120, -64), pya.Point(1120, 1120), pya.Point(1048, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_39)

polygon_N5_40 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 688), pya.Point(616, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_40)

polygon_N5_41 = pya.Polygon([ pya.Point(1336, -64), pya.Point(1408, -64), pya.Point(1408, 1120), pya.Point(1336, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_41)

polygon_N6_42 = pya.Polygon([ pya.Point(1768, 944), pya.Point(1840, 944), pya.Point(1840, 1120), pya.Point(1768, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_42)

polygon_N7_43 = pya.Polygon([ pya.Point(616, 800), pya.Point(688, 800), pya.Point(688, 976), pya.Point(616, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_43)

polygon_N8_44 = pya.Polygon([ pya.Point(1624, 80), pya.Point(1696, 80), pya.Point(1696, 976), pya.Point(1624, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_44)

polygon_N9_45 = pya.Polygon([ pya.Point(760, 656), pya.Point(832, 656), pya.Point(832, 832), pya.Point(760, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_45)

polygon_N2_46 = pya.Polygon([ pya.Point(40, 1004), pya.Point(112, 1004), pya.Point(112, 1076), pya.Point(40, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_46)

polygon_N2_47 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_47)

polygon_N2_48 = pya.Polygon([ pya.Point(40, -4), pya.Point(112, -4), pya.Point(112, 68), pya.Point(40, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_48)

polygon_N2_49 = pya.Polygon([ pya.Point(328, -4), pya.Point(400, -4), pya.Point(400, 68), pya.Point(328, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_49)

polygon_N3_50 = pya.Polygon([ pya.Point(472, 1004), pya.Point(544, 1004), pya.Point(544, 1076), pya.Point(472, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_50)

polygon_N3_51 = pya.Polygon([ pya.Point(184, 716), pya.Point(256, 716), pya.Point(256, 788), pya.Point(184, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_51)

polygon_N3_52 = pya.Polygon([ pya.Point(184, 140), pya.Point(256, 140), pya.Point(256, 212), pya.Point(184, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_52)

polygon_N3_53 = pya.Polygon([ pya.Point(472, 140), pya.Point(544, 140), pya.Point(544, 212), pya.Point(472, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_53)

polygon_N4_54 = pya.Polygon([ pya.Point(1048, 1004), pya.Point(1120, 1004), pya.Point(1120, 1076), pya.Point(1048, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_54)

polygon_N4_55 = pya.Polygon([ pya.Point(1048, 428), pya.Point(1120, 428), pya.Point(1120, 500), pya.Point(1048, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_55)

polygon_N4_56 = pya.Polygon([ pya.Point(1048, -4), pya.Point(1120, -4), pya.Point(1120, 68), pya.Point(1048, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_56)

polygon_N5_57 = pya.Polygon([ pya.Point(1336, 1004), pya.Point(1408, 1004), pya.Point(1408, 1076), pya.Point(1336, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_57)

polygon_N5_58 = pya.Polygon([ pya.Point(616, 572), pya.Point(688, 572), pya.Point(688, 644), pya.Point(616, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_58)

polygon_N5_59 = pya.Polygon([ pya.Point(1336, 572), pya.Point(1408, 572), pya.Point(1408, 644), pya.Point(1336, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_59)

polygon_N5_60 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_60)

polygon_N5_61 = pya.Polygon([ pya.Point(1336, -4), pya.Point(1408, -4), pya.Point(1408, 68), pya.Point(1336, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_61)

polygon_N6_62 = pya.Polygon([ pya.Point(1768, 1004), pya.Point(1840, 1004), pya.Point(1840, 1076), pya.Point(1768, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_62)

polygon_N7_63 = pya.Polygon([ pya.Point(616, 860), pya.Point(688, 860), pya.Point(688, 932), pya.Point(616, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_63)

polygon_N8_64 = pya.Polygon([ pya.Point(1624, 860), pya.Point(1696, 860), pya.Point(1696, 932), pya.Point(1624, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_64)

polygon_N8_65 = pya.Polygon([ pya.Point(1624, 140), pya.Point(1696, 140), pya.Point(1696, 212), pya.Point(1624, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_65)

polygon_N9_66 = pya.Polygon([ pya.Point(760, 716), pya.Point(832, 716), pya.Point(832, 788), pya.Point(760, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_66)

polygon_N10_67 = pya.Polygon([ pya.Point(904, 716), pya.Point(976, 716), pya.Point(976, 788), pya.Point(904, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_67)

polygon_N10_68 = pya.Polygon([ pya.Point(904, 284), pya.Point(976, 284), pya.Point(976, 356), pya.Point(904, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_68)

polygon_N11_69 = pya.Polygon([ pya.Point(1192, 716), pya.Point(1264, 716), pya.Point(1264, 788), pya.Point(1192, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_69)

polygon_N11_70 = pya.Polygon([ pya.Point(1192, 140), pya.Point(1264, 140), pya.Point(1264, 212), pya.Point(1192, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_70)

polygon_N12_71 = pya.Polygon([ pya.Point(1480, 716), pya.Point(1552, 716), pya.Point(1552, 788), pya.Point(1480, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_71)

polygon_N13_72 = pya.Polygon([ pya.Point(1768, 716), pya.Point(1840, 716), pya.Point(1840, 788), pya.Point(1768, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_72)

polygon_N13_73 = pya.Polygon([ pya.Point(1768, 428), pya.Point(1840, 428), pya.Point(1840, 500), pya.Point(1768, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_73)

polygon_N13_74 = pya.Polygon([ pya.Point(1768, -4), pya.Point(1840, -4), pya.Point(1840, 68), pya.Point(1768, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_74)

polygon_N15_75 = pya.Polygon([ pya.Point(760, 140), pya.Point(832, 140), pya.Point(832, 212), pya.Point(760, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N15_75)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1848, -64), pya.Point(1848, 1220), pya.Point(16, 1220)]))

layout.write("../gds/Cell134.gds")
