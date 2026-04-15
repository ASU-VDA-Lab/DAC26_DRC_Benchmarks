import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell4")

polygon_N1_0 = pya.Polygon([ pya.Point(520, 716), pya.Point(696, 716), pya.Point(696, 788), pya.Point(520, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(592, 1148), pya.Point(1200, 1148), pya.Point(1200, 1220), pya.Point(592, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N10_2 = pya.Polygon([ pya.Point(304, 284), pya.Point(552, 284), pya.Point(552, 356), pya.Point(304, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_2)

polygon_N10_3 = pya.Polygon([ pya.Point(304, 572), pya.Point(1560, 572), pya.Point(1560, 644), pya.Point(304, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_3)

polygon_N10_4 = pya.Polygon([ pya.Point(1456, 284), pya.Point(1632, 284), pya.Point(1632, 356), pya.Point(1456, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_4)

polygon_N11_5 = pya.Polygon([ pya.Point(736, -4), pya.Point(912, -4), pya.Point(912, 68), pya.Point(736, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_5)

polygon_N11_6 = pya.Polygon([ pya.Point(304, 428), pya.Point(624, 428), pya.Point(624, 500), pya.Point(304, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_6)

polygon_N12_7 = pya.Polygon([ pya.Point(232, -4), pya.Point(696, -4), pya.Point(696, 68), pya.Point(232, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_7)

polygon_N12_8 = pya.Polygon([ pya.Point(592, 284), pya.Point(912, 284), pya.Point(912, 356), pya.Point(592, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_8)

polygon_N13_9 = pya.Polygon([ pya.Point(16, -4), pya.Point(192, -4), pya.Point(192, 68), pya.Point(16, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_9)

polygon_N14_10 = pya.Polygon([ pya.Point(1528, -4), pya.Point(1704, -4), pya.Point(1704, 68), pya.Point(1528, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_10)

polygon_N2_11 = pya.Polygon([ pya.Point(736, 716), pya.Point(1272, 716), pya.Point(1272, 788), pya.Point(736, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_11)

polygon_N2_12 = pya.Polygon([ pya.Point(520, 1004), pya.Point(840, 1004), pya.Point(840, 1076), pya.Point(520, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_12)

polygon_N3_13 = pya.Polygon([ pya.Point(880, 428), pya.Point(1056, 428), pya.Point(1056, 500), pya.Point(880, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_13)

polygon_N3_14 = pya.Polygon([ pya.Point(880, 1004), pya.Point(1704, 1004), pya.Point(1704, 1076), pya.Point(880, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_14)

polygon_N4_15 = pya.Polygon([ pya.Point(16, 284), pya.Point(192, 284), pya.Point(192, 356), pya.Point(16, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_15)

polygon_N4_16 = pya.Polygon([ pya.Point(16, 860), pya.Point(840, 860), pya.Point(840, 932), pya.Point(16, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_16)

polygon_N5_17 = pya.Polygon([ pya.Point(1024, 140), pya.Point(1416, 140), pya.Point(1416, 212), pya.Point(1024, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_17)

polygon_N5_18 = pya.Polygon([ pya.Point(952, 860), pya.Point(1128, 860), pya.Point(1128, 932), pya.Point(952, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_18)

polygon_N6_19 = pya.Polygon([ pya.Point(952, -4), pya.Point(1272, -4), pya.Point(1272, 68), pya.Point(952, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_19)

polygon_N6_20 = pya.Polygon([ pya.Point(1168, 428), pya.Point(1488, 428), pya.Point(1488, 500), pya.Point(1168, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_20)

polygon_N6_21 = pya.Polygon([ pya.Point(1168, 860), pya.Point(1416, 860), pya.Point(1416, 932), pya.Point(1168, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_21)

polygon_N7_22 = pya.Polygon([ pya.Point(160, 140), pya.Point(840, 140), pya.Point(840, 212), pya.Point(160, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_22)

polygon_N7_23 = pya.Polygon([ pya.Point(160, 716), pya.Point(480, 716), pya.Point(480, 788), pya.Point(160, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_23)

polygon_N8_24 = pya.Polygon([ pya.Point(1312, -4), pya.Point(1488, -4), pya.Point(1488, 68), pya.Point(1312, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_24)

polygon_N8_25 = pya.Polygon([ pya.Point(952, 284), pya.Point(1416, 284), pya.Point(1416, 356), pya.Point(952, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_25)

polygon_N8_26 = pya.Polygon([ pya.Point(1312, 716), pya.Point(1488, 716), pya.Point(1488, 788), pya.Point(1312, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_26)

polygon_N9_27 = pya.Polygon([ pya.Point(1528, 716), pya.Point(1704, 716), pya.Point(1704, 788), pya.Point(1528, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_27)

polygon_N1_28 = pya.Polygon([ pya.Point(616, 656), pya.Point(688, 656), pya.Point(688, 1264), pya.Point(616, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_28)

polygon_N10_29 = pya.Polygon([ pya.Point(328, 224), pya.Point(400, 224), pya.Point(400, 688), pya.Point(328, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_29)

polygon_N10_30 = pya.Polygon([ pya.Point(1480, 224), pya.Point(1552, 224), pya.Point(1552, 688), pya.Point(1480, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_30)

polygon_N11_31 = pya.Polygon([ pya.Point(472, -64), pya.Point(544, -64), pya.Point(544, 544), pya.Point(472, 544), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_31)

polygon_N11_32 = pya.Polygon([ pya.Point(760, -64), pya.Point(832, -64), pya.Point(832, 112), pya.Point(760, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_32)

polygon_N12_33 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 400), pya.Point(616, 400), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N12_33)

polygon_N13_34 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 112), pya.Point(40, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N13_34)

polygon_N14_35 = pya.Polygon([ pya.Point(1624, -64), pya.Point(1696, -64), pya.Point(1696, 112), pya.Point(1624, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N14_35)

polygon_N2_36 = pya.Polygon([ pya.Point(760, 656), pya.Point(832, 656), pya.Point(832, 1120), pya.Point(760, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_36)

polygon_N3_37 = pya.Polygon([ pya.Point(904, 368), pya.Point(976, 368), pya.Point(976, 1120), pya.Point(904, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_37)

polygon_N4_38 = pya.Polygon([ pya.Point(40, 224), pya.Point(112, 224), pya.Point(112, 976), pya.Point(40, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_38)

polygon_N5_39 = pya.Polygon([ pya.Point(1048, 80), pya.Point(1120, 80), pya.Point(1120, 976), pya.Point(1048, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_39)

polygon_N6_40 = pya.Polygon([ pya.Point(1192, -64), pya.Point(1264, -64), pya.Point(1264, 976), pya.Point(1192, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_40)

polygon_N7_41 = pya.Polygon([ pya.Point(184, 80), pya.Point(256, 80), pya.Point(256, 832), pya.Point(184, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_41)

polygon_N8_42 = pya.Polygon([ pya.Point(1336, -64), pya.Point(1408, -64), pya.Point(1408, 832), pya.Point(1336, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_42)

polygon_N9_43 = pya.Polygon([ pya.Point(1624, 656), pya.Point(1696, 656), pya.Point(1696, 832), pya.Point(1624, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_43)

polygon_N11_44 = pya.Polygon([ pya.Point(416, -4), pya.Point(960, -4), pya.Point(960, 68), pya.Point(416, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(20, 0))).insert(polygon_N11_44)

polygon_N1_45 = pya.Polygon([ pya.Point(616, 1148), pya.Point(688, 1148), pya.Point(688, 1220), pya.Point(616, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_45)

polygon_N1_46 = pya.Polygon([ pya.Point(616, 716), pya.Point(688, 716), pya.Point(688, 788), pya.Point(616, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_46)

polygon_N2_47 = pya.Polygon([ pya.Point(760, 1004), pya.Point(832, 1004), pya.Point(832, 1076), pya.Point(760, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_47)

polygon_N2_48 = pya.Polygon([ pya.Point(760, 716), pya.Point(832, 716), pya.Point(832, 788), pya.Point(760, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_48)

polygon_N3_49 = pya.Polygon([ pya.Point(904, 1004), pya.Point(976, 1004), pya.Point(976, 1076), pya.Point(904, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_49)

polygon_N3_50 = pya.Polygon([ pya.Point(904, 428), pya.Point(976, 428), pya.Point(976, 500), pya.Point(904, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_50)

polygon_N4_51 = pya.Polygon([ pya.Point(40, 860), pya.Point(112, 860), pya.Point(112, 932), pya.Point(40, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_51)

polygon_N4_52 = pya.Polygon([ pya.Point(40, 284), pya.Point(112, 284), pya.Point(112, 356), pya.Point(40, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_52)

polygon_N5_53 = pya.Polygon([ pya.Point(1048, 860), pya.Point(1120, 860), pya.Point(1120, 932), pya.Point(1048, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_53)

polygon_N5_54 = pya.Polygon([ pya.Point(1048, 140), pya.Point(1120, 140), pya.Point(1120, 212), pya.Point(1048, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_54)

polygon_N6_55 = pya.Polygon([ pya.Point(1192, 860), pya.Point(1264, 860), pya.Point(1264, 932), pya.Point(1192, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_55)

polygon_N6_56 = pya.Polygon([ pya.Point(1192, 428), pya.Point(1264, 428), pya.Point(1264, 500), pya.Point(1192, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_56)

polygon_N6_57 = pya.Polygon([ pya.Point(1192, -4), pya.Point(1264, -4), pya.Point(1264, 68), pya.Point(1192, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_57)

polygon_N7_58 = pya.Polygon([ pya.Point(184, 716), pya.Point(256, 716), pya.Point(256, 788), pya.Point(184, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_58)

polygon_N7_59 = pya.Polygon([ pya.Point(184, 140), pya.Point(256, 140), pya.Point(256, 212), pya.Point(184, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_59)

polygon_N8_60 = pya.Polygon([ pya.Point(1336, 716), pya.Point(1408, 716), pya.Point(1408, 788), pya.Point(1336, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_60)

polygon_N8_61 = pya.Polygon([ pya.Point(1336, 284), pya.Point(1408, 284), pya.Point(1408, 356), pya.Point(1336, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_61)

polygon_N8_62 = pya.Polygon([ pya.Point(1336, -4), pya.Point(1408, -4), pya.Point(1408, 68), pya.Point(1336, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_62)

polygon_N9_63 = pya.Polygon([ pya.Point(1624, 716), pya.Point(1696, 716), pya.Point(1696, 788), pya.Point(1624, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_63)

polygon_N10_64 = pya.Polygon([ pya.Point(328, 572), pya.Point(400, 572), pya.Point(400, 644), pya.Point(328, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_64)

polygon_N10_65 = pya.Polygon([ pya.Point(1480, 572), pya.Point(1552, 572), pya.Point(1552, 644), pya.Point(1480, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_65)

polygon_N10_66 = pya.Polygon([ pya.Point(328, 284), pya.Point(400, 284), pya.Point(400, 356), pya.Point(328, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_66)

polygon_N10_67 = pya.Polygon([ pya.Point(1480, 284), pya.Point(1552, 284), pya.Point(1552, 356), pya.Point(1480, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_67)

polygon_N11_68 = pya.Polygon([ pya.Point(472, 428), pya.Point(544, 428), pya.Point(544, 500), pya.Point(472, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_68)

polygon_N11_69 = pya.Polygon([ pya.Point(760, -4), pya.Point(832, -4), pya.Point(832, 68), pya.Point(760, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_69)

polygon_N12_70 = pya.Polygon([ pya.Point(616, 284), pya.Point(688, 284), pya.Point(688, 356), pya.Point(616, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_70)

polygon_N12_71 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_71)

polygon_N13_72 = pya.Polygon([ pya.Point(40, -4), pya.Point(112, -4), pya.Point(112, 68), pya.Point(40, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_72)

polygon_N14_73 = pya.Polygon([ pya.Point(1624, -4), pya.Point(1696, -4), pya.Point(1696, 68), pya.Point(1624, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_73)

polygon_N11_74 = pya.Polygon([ pya.Point(472, -4), pya.Point(544, -4), pya.Point(544, 68), pya.Point(472, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(21, 0))).insert(polygon_N11_74)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1704, -64), pya.Point(1704, 1264), pya.Point(16, 1264)]))

layout.write("../gds/Cell4.gds")
