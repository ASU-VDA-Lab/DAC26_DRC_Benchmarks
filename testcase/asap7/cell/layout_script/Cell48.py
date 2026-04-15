import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell48")

polygon_N1_0 = pya.Polygon([ pya.Point(88, 1148), pya.Point(1560, 1148), pya.Point(1560, 1220), pya.Point(88, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(1240, 716), pya.Point(1560, 716), pya.Point(1560, 788), pya.Point(1240, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N10_2 = pya.Polygon([ pya.Point(808, 716), pya.Point(984, 716), pya.Point(984, 788), pya.Point(808, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_2)

polygon_N11_3 = pya.Polygon([ pya.Point(1024, 284), pya.Point(1848, 284), pya.Point(1848, 356), pya.Point(1024, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_3)

polygon_N11_4 = pya.Polygon([ pya.Point(1600, 716), pya.Point(2280, 716), pya.Point(2280, 788), pya.Point(1600, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_4)

polygon_N12_5 = pya.Polygon([ pya.Point(664, 428), pya.Point(1920, 428), pya.Point(1920, 500), pya.Point(664, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_5)

polygon_N12_6 = pya.Polygon([ pya.Point(1816, 140), pya.Point(2208, 140), pya.Point(2208, 212), pya.Point(1816, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_6)

polygon_N13_7 = pya.Polygon([ pya.Point(448, 284), pya.Point(912, 284), pya.Point(912, 356), pya.Point(448, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_7)

polygon_N14_8 = pya.Polygon([ pya.Point(1456, -4), pya.Point(2136, -4), pya.Point(2136, 68), pya.Point(1456, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_8)

polygon_N2_9 = pya.Polygon([ pya.Point(304, -4), pya.Point(480, -4), pya.Point(480, 68), pya.Point(304, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_9)

polygon_N2_10 = pya.Polygon([ pya.Point(16, 428), pya.Point(624, 428), pya.Point(624, 500), pya.Point(16, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_10)

polygon_N2_11 = pya.Polygon([ pya.Point(304, 1004), pya.Point(480, 1004), pya.Point(480, 1076), pya.Point(304, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_11)

polygon_N3_12 = pya.Polygon([ pya.Point(16, -4), pya.Point(264, -4), pya.Point(264, 68), pya.Point(16, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_12)

polygon_N3_13 = pya.Polygon([ pya.Point(16, 572), pya.Point(840, 572), pya.Point(840, 644), pya.Point(16, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_13)

polygon_N3_14 = pya.Polygon([ pya.Point(520, -4), pya.Point(840, -4), pya.Point(840, 68), pya.Point(520, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_14)

polygon_N3_15 = pya.Polygon([ pya.Point(520, 1004), pya.Point(840, 1004), pya.Point(840, 1076), pya.Point(520, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_15)

polygon_N4_16 = pya.Polygon([ pya.Point(880, 1004), pya.Point(1056, 1004), pya.Point(1056, 1076), pya.Point(880, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_16)

polygon_N5_17 = pya.Polygon([ pya.Point(16, 860), pya.Point(1128, 860), pya.Point(1128, 932), pya.Point(16, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_17)

polygon_N5_18 = pya.Polygon([ pya.Point(1024, -4), pya.Point(1416, -4), pya.Point(1416, 68), pya.Point(1024, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_18)

polygon_N5_19 = pya.Polygon([ pya.Point(1024, 716), pya.Point(1200, 716), pya.Point(1200, 788), pya.Point(1024, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_19)

polygon_N5_20 = pya.Polygon([ pya.Point(1240, 1004), pya.Point(1488, 1004), pya.Point(1488, 1076), pya.Point(1240, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_20)

polygon_N6_21 = pya.Polygon([ pya.Point(592, 716), pya.Point(768, 716), pya.Point(768, 788), pya.Point(592, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_21)

polygon_N6_22 = pya.Polygon([ pya.Point(1168, 860), pya.Point(1344, 860), pya.Point(1344, 932), pya.Point(1168, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_22)

polygon_N7_23 = pya.Polygon([ pya.Point(592, 140), pya.Point(1704, 140), pya.Point(1704, 212), pya.Point(592, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_23)

polygon_N7_24 = pya.Polygon([ pya.Point(1384, 860), pya.Point(2208, 860), pya.Point(2208, 932), pya.Point(1384, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_24)

polygon_N8_25 = pya.Polygon([ pya.Point(160, 284), pya.Point(408, 284), pya.Point(408, 356), pya.Point(160, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_25)

polygon_N8_26 = pya.Polygon([ pya.Point(160, 716), pya.Point(336, 716), pya.Point(336, 788), pya.Point(160, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_26)

polygon_N9_27 = pya.Polygon([ pya.Point(232, 140), pya.Point(552, 140), pya.Point(552, 212), pya.Point(232, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_27)

polygon_N9_28 = pya.Polygon([ pya.Point(376, 716), pya.Point(552, 716), pya.Point(552, 788), pya.Point(376, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_28)

polygon_N1_29 = pya.Polygon([ pya.Point(1480, 656), pya.Point(1552, 656), pya.Point(1552, 1264), pya.Point(1480, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_29)

polygon_N10_30 = pya.Polygon([ pya.Point(904, 656), pya.Point(976, 656), pya.Point(976, 832), pya.Point(904, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_30)

polygon_N11_31 = pya.Polygon([ pya.Point(1768, 224), pya.Point(1840, 224), pya.Point(1840, 832), pya.Point(1768, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_31)

polygon_N14_32 = pya.Polygon([ pya.Point(1768, -64), pya.Point(1840, -64), pya.Point(1840, 112), pya.Point(1768, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N14_32)

polygon_N2_33 = pya.Polygon([ pya.Point(328, -64), pya.Point(400, -64), pya.Point(400, 1120), pya.Point(328, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_33)

polygon_N3_34 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 688), pya.Point(40, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_34)

polygon_N3_35 = pya.Polygon([ pya.Point(760, -64), pya.Point(832, -64), pya.Point(832, 1120), pya.Point(760, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_35)

polygon_N4_36 = pya.Polygon([ pya.Point(904, 944), pya.Point(976, 944), pya.Point(976, 1120), pya.Point(904, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_36)

polygon_N5_37 = pya.Polygon([ pya.Point(1048, -64), pya.Point(1120, -64), pya.Point(1120, 976), pya.Point(1048, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_37)

polygon_N5_38 = pya.Polygon([ pya.Point(1336, -64), pya.Point(1408, -64), pya.Point(1408, 1120), pya.Point(1336, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_38)

polygon_N6_39 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 832), pya.Point(616, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_39)

polygon_N6_40 = pya.Polygon([ pya.Point(1192, -64), pya.Point(1264, -64), pya.Point(1264, 976), pya.Point(1192, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_40)

polygon_N7_41 = pya.Polygon([ pya.Point(1624, 80), pya.Point(1696, 80), pya.Point(1696, 976), pya.Point(1624, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_41)

polygon_N8_42 = pya.Polygon([ pya.Point(184, 224), pya.Point(256, 224), pya.Point(256, 832), pya.Point(184, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_42)

polygon_N9_43 = pya.Polygon([ pya.Point(472, 80), pya.Point(544, 80), pya.Point(544, 832), pya.Point(472, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_43)

polygon_N6_44 = pya.Polygon([ pya.Point(560, -4), pya.Point(1392, -4), pya.Point(1392, 68), pya.Point(560, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(20, 0))).insert(polygon_N6_44)

polygon_N1_45 = pya.Polygon([ pya.Point(1480, 1148), pya.Point(1552, 1148), pya.Point(1552, 1220), pya.Point(1480, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_45)

polygon_N1_46 = pya.Polygon([ pya.Point(1480, 716), pya.Point(1552, 716), pya.Point(1552, 788), pya.Point(1480, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_46)

polygon_N2_47 = pya.Polygon([ pya.Point(328, 1004), pya.Point(400, 1004), pya.Point(400, 1076), pya.Point(328, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_47)

polygon_N2_48 = pya.Polygon([ pya.Point(328, 428), pya.Point(400, 428), pya.Point(400, 500), pya.Point(328, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_48)

polygon_N2_49 = pya.Polygon([ pya.Point(328, -4), pya.Point(400, -4), pya.Point(400, 68), pya.Point(328, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_49)

polygon_N3_50 = pya.Polygon([ pya.Point(760, 1004), pya.Point(832, 1004), pya.Point(832, 1076), pya.Point(760, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_50)

polygon_N3_51 = pya.Polygon([ pya.Point(40, 572), pya.Point(112, 572), pya.Point(112, 644), pya.Point(40, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_51)

polygon_N3_52 = pya.Polygon([ pya.Point(760, 572), pya.Point(832, 572), pya.Point(832, 644), pya.Point(760, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_52)

polygon_N3_53 = pya.Polygon([ pya.Point(40, -4), pya.Point(112, -4), pya.Point(112, 68), pya.Point(40, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_53)

polygon_N3_54 = pya.Polygon([ pya.Point(760, -4), pya.Point(832, -4), pya.Point(832, 68), pya.Point(760, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_54)

polygon_N4_55 = pya.Polygon([ pya.Point(904, 1004), pya.Point(976, 1004), pya.Point(976, 1076), pya.Point(904, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_55)

polygon_N5_56 = pya.Polygon([ pya.Point(1336, 1004), pya.Point(1408, 1004), pya.Point(1408, 1076), pya.Point(1336, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_56)

polygon_N5_57 = pya.Polygon([ pya.Point(1048, 860), pya.Point(1120, 860), pya.Point(1120, 932), pya.Point(1048, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_57)

polygon_N5_58 = pya.Polygon([ pya.Point(1048, 716), pya.Point(1120, 716), pya.Point(1120, 788), pya.Point(1048, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_58)

polygon_N5_59 = pya.Polygon([ pya.Point(1048, -4), pya.Point(1120, -4), pya.Point(1120, 68), pya.Point(1048, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_59)

polygon_N5_60 = pya.Polygon([ pya.Point(1336, -4), pya.Point(1408, -4), pya.Point(1408, 68), pya.Point(1336, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_60)

polygon_N6_61 = pya.Polygon([ pya.Point(1192, 860), pya.Point(1264, 860), pya.Point(1264, 932), pya.Point(1192, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_61)

polygon_N6_62 = pya.Polygon([ pya.Point(616, 716), pya.Point(688, 716), pya.Point(688, 788), pya.Point(616, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_62)

polygon_N7_63 = pya.Polygon([ pya.Point(1624, 860), pya.Point(1696, 860), pya.Point(1696, 932), pya.Point(1624, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_63)

polygon_N7_64 = pya.Polygon([ pya.Point(1624, 140), pya.Point(1696, 140), pya.Point(1696, 212), pya.Point(1624, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_64)

polygon_N8_65 = pya.Polygon([ pya.Point(184, 716), pya.Point(256, 716), pya.Point(256, 788), pya.Point(184, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_65)

polygon_N8_66 = pya.Polygon([ pya.Point(184, 284), pya.Point(256, 284), pya.Point(256, 356), pya.Point(184, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_66)

polygon_N9_67 = pya.Polygon([ pya.Point(472, 716), pya.Point(544, 716), pya.Point(544, 788), pya.Point(472, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_67)

polygon_N9_68 = pya.Polygon([ pya.Point(472, 140), pya.Point(544, 140), pya.Point(544, 212), pya.Point(472, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_68)

polygon_N10_69 = pya.Polygon([ pya.Point(904, 716), pya.Point(976, 716), pya.Point(976, 788), pya.Point(904, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_69)

polygon_N11_70 = pya.Polygon([ pya.Point(1768, 716), pya.Point(1840, 716), pya.Point(1840, 788), pya.Point(1768, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_70)

polygon_N11_71 = pya.Polygon([ pya.Point(1768, 284), pya.Point(1840, 284), pya.Point(1840, 356), pya.Point(1768, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_71)

polygon_N14_72 = pya.Polygon([ pya.Point(1768, -4), pya.Point(1840, -4), pya.Point(1840, 68), pya.Point(1768, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_72)

polygon_N6_73 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(21, 0))).insert(polygon_N6_73)

polygon_N6_74 = pya.Polygon([ pya.Point(1192, -4), pya.Point(1264, -4), pya.Point(1264, 68), pya.Point(1192, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(21, 0))).insert(polygon_N6_74)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(2280, -64), pya.Point(2280, 1264), pya.Point(16, 1264)]))

layout.write("../gds/Cell48.gds")
