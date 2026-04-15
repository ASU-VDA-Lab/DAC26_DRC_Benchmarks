import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell7")

polygon_N1_0 = pya.Polygon([ pya.Point(520, 716), pya.Point(696, 716), pya.Point(696, 788), pya.Point(520, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(592, 1148), pya.Point(1200, 1148), pya.Point(1200, 1220), pya.Point(592, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N10_2 = pya.Polygon([ pya.Point(376, 284), pya.Point(552, 284), pya.Point(552, 356), pya.Point(376, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_2)

polygon_N10_3 = pya.Polygon([ pya.Point(448, 572), pya.Point(1560, 572), pya.Point(1560, 644), pya.Point(448, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_3)

polygon_N10_4 = pya.Polygon([ pya.Point(1456, 140), pya.Point(1632, 140), pya.Point(1632, 212), pya.Point(1456, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_4)

polygon_N11_5 = pya.Polygon([ pya.Point(736, -4), pya.Point(912, -4), pya.Point(912, 68), pya.Point(736, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_5)

polygon_N11_6 = pya.Polygon([ pya.Point(304, 428), pya.Point(840, 428), pya.Point(840, 500), pya.Point(304, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_6)

polygon_N12_7 = pya.Polygon([ pya.Point(232, -4), pya.Point(696, -4), pya.Point(696, 68), pya.Point(232, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_7)

polygon_N12_8 = pya.Polygon([ pya.Point(592, 284), pya.Point(912, 284), pya.Point(912, 356), pya.Point(592, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_8)

polygon_N13_9 = pya.Polygon([ pya.Point(16, -4), pya.Point(192, -4), pya.Point(192, 68), pya.Point(16, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_9)

polygon_N14_10 = pya.Polygon([ pya.Point(1528, -4), pya.Point(1704, -4), pya.Point(1704, 68), pya.Point(1528, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_10)

polygon_N2_11 = pya.Polygon([ pya.Point(736, 716), pya.Point(912, 716), pya.Point(912, 788), pya.Point(736, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_11)

polygon_N2_12 = pya.Polygon([ pya.Point(520, 1004), pya.Point(1272, 1004), pya.Point(1272, 1076), pya.Point(520, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_12)

polygon_N3_13 = pya.Polygon([ pya.Point(88, 140), pya.Point(264, 140), pya.Point(264, 212), pya.Point(88, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_13)

polygon_N3_14 = pya.Polygon([ pya.Point(160, 860), pya.Point(840, 860), pya.Point(840, 932), pya.Point(160, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_14)

polygon_N4_15 = pya.Polygon([ pya.Point(880, 140), pya.Point(1416, 140), pya.Point(1416, 212), pya.Point(880, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_15)

polygon_N4_16 = pya.Polygon([ pya.Point(880, 860), pya.Point(1056, 860), pya.Point(1056, 932), pya.Point(880, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_16)

polygon_N5_17 = pya.Polygon([ pya.Point(952, -4), pya.Point(1272, -4), pya.Point(1272, 68), pya.Point(952, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_17)

polygon_N5_18 = pya.Polygon([ pya.Point(1168, 284), pya.Point(1488, 284), pya.Point(1488, 356), pya.Point(1168, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_18)

polygon_N5_19 = pya.Polygon([ pya.Point(1168, 860), pya.Point(1416, 860), pya.Point(1416, 932), pya.Point(1168, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_19)

polygon_N6_20 = pya.Polygon([ pya.Point(1456, 860), pya.Point(1632, 860), pya.Point(1632, 932), pya.Point(1456, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_20)

polygon_N7_21 = pya.Polygon([ pya.Point(304, 140), pya.Point(840, 140), pya.Point(840, 212), pya.Point(304, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_21)

polygon_N7_22 = pya.Polygon([ pya.Point(304, 716), pya.Point(480, 716), pya.Point(480, 788), pya.Point(304, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_22)

polygon_N8_23 = pya.Polygon([ pya.Point(1312, -4), pya.Point(1488, -4), pya.Point(1488, 68), pya.Point(1312, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_23)

polygon_N8_24 = pya.Polygon([ pya.Point(952, 284), pya.Point(1128, 284), pya.Point(1128, 356), pya.Point(952, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_24)

polygon_N8_25 = pya.Polygon([ pya.Point(1024, 716), pya.Point(1488, 716), pya.Point(1488, 788), pya.Point(1024, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_25)

polygon_N9_26 = pya.Polygon([ pya.Point(880, 428), pya.Point(1704, 428), pya.Point(1704, 500), pya.Point(880, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_26)

polygon_N9_27 = pya.Polygon([ pya.Point(1528, 716), pya.Point(1704, 716), pya.Point(1704, 788), pya.Point(1528, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_27)

polygon_N1_28 = pya.Polygon([ pya.Point(616, 656), pya.Point(688, 656), pya.Point(688, 1264), pya.Point(616, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_28)

polygon_N10_29 = pya.Polygon([ pya.Point(1480, 80), pya.Point(1552, 80), pya.Point(1552, 688), pya.Point(1480, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_29)

polygon_N10_30 = pya.Polygon([ pya.Point(472, 224), pya.Point(544, 224), pya.Point(544, 688), pya.Point(472, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_30)

polygon_N11_31 = pya.Polygon([ pya.Point(760, -64), pya.Point(832, -64), pya.Point(832, 544), pya.Point(760, 544), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_31)

polygon_N12_32 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 400), pya.Point(616, 400), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N12_32)

polygon_N13_33 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 112), pya.Point(40, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N13_33)

polygon_N14_34 = pya.Polygon([ pya.Point(1624, -64), pya.Point(1696, -64), pya.Point(1696, 112), pya.Point(1624, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N14_34)

polygon_N2_35 = pya.Polygon([ pya.Point(760, 656), pya.Point(832, 656), pya.Point(832, 1120), pya.Point(760, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_35)

polygon_N3_36 = pya.Polygon([ pya.Point(184, 80), pya.Point(256, 80), pya.Point(256, 976), pya.Point(184, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_36)

polygon_N4_37 = pya.Polygon([ pya.Point(904, 80), pya.Point(976, 80), pya.Point(976, 976), pya.Point(904, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_37)

polygon_N5_38 = pya.Polygon([ pya.Point(1192, -64), pya.Point(1264, -64), pya.Point(1264, 976), pya.Point(1192, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_38)

polygon_N6_39 = pya.Polygon([ pya.Point(1480, 800), pya.Point(1552, 800), pya.Point(1552, 976), pya.Point(1480, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_39)

polygon_N7_40 = pya.Polygon([ pya.Point(328, 80), pya.Point(400, 80), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_40)

polygon_N8_41 = pya.Polygon([ pya.Point(1336, -64), pya.Point(1408, -64), pya.Point(1408, 832), pya.Point(1336, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_41)

polygon_N8_42 = pya.Polygon([ pya.Point(1048, 224), pya.Point(1120, 224), pya.Point(1120, 832), pya.Point(1048, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_42)

polygon_N9_43 = pya.Polygon([ pya.Point(1624, 368), pya.Point(1696, 368), pya.Point(1696, 832), pya.Point(1624, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_43)

polygon_N1_44 = pya.Polygon([ pya.Point(616, 1148), pya.Point(688, 1148), pya.Point(688, 1220), pya.Point(616, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_44)

polygon_N1_45 = pya.Polygon([ pya.Point(616, 716), pya.Point(688, 716), pya.Point(688, 788), pya.Point(616, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_45)

polygon_N2_46 = pya.Polygon([ pya.Point(760, 1004), pya.Point(832, 1004), pya.Point(832, 1076), pya.Point(760, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_46)

polygon_N2_47 = pya.Polygon([ pya.Point(760, 716), pya.Point(832, 716), pya.Point(832, 788), pya.Point(760, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_47)

polygon_N3_48 = pya.Polygon([ pya.Point(184, 860), pya.Point(256, 860), pya.Point(256, 932), pya.Point(184, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_48)

polygon_N3_49 = pya.Polygon([ pya.Point(184, 140), pya.Point(256, 140), pya.Point(256, 212), pya.Point(184, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_49)

polygon_N4_50 = pya.Polygon([ pya.Point(904, 860), pya.Point(976, 860), pya.Point(976, 932), pya.Point(904, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_50)

polygon_N4_51 = pya.Polygon([ pya.Point(904, 140), pya.Point(976, 140), pya.Point(976, 212), pya.Point(904, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_51)

polygon_N5_52 = pya.Polygon([ pya.Point(1192, 860), pya.Point(1264, 860), pya.Point(1264, 932), pya.Point(1192, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_52)

polygon_N5_53 = pya.Polygon([ pya.Point(1192, 284), pya.Point(1264, 284), pya.Point(1264, 356), pya.Point(1192, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_53)

polygon_N5_54 = pya.Polygon([ pya.Point(1192, -4), pya.Point(1264, -4), pya.Point(1264, 68), pya.Point(1192, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_54)

polygon_N6_55 = pya.Polygon([ pya.Point(1480, 860), pya.Point(1552, 860), pya.Point(1552, 932), pya.Point(1480, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_55)

polygon_N7_56 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_56)

polygon_N7_57 = pya.Polygon([ pya.Point(328, 140), pya.Point(400, 140), pya.Point(400, 212), pya.Point(328, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_57)

polygon_N8_58 = pya.Polygon([ pya.Point(1048, 716), pya.Point(1120, 716), pya.Point(1120, 788), pya.Point(1048, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_58)

polygon_N8_59 = pya.Polygon([ pya.Point(1336, 716), pya.Point(1408, 716), pya.Point(1408, 788), pya.Point(1336, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_59)

polygon_N8_60 = pya.Polygon([ pya.Point(1048, 284), pya.Point(1120, 284), pya.Point(1120, 356), pya.Point(1048, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_60)

polygon_N8_61 = pya.Polygon([ pya.Point(1336, -4), pya.Point(1408, -4), pya.Point(1408, 68), pya.Point(1336, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_61)

polygon_N9_62 = pya.Polygon([ pya.Point(1624, 716), pya.Point(1696, 716), pya.Point(1696, 788), pya.Point(1624, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_62)

polygon_N9_63 = pya.Polygon([ pya.Point(1624, 428), pya.Point(1696, 428), pya.Point(1696, 500), pya.Point(1624, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_63)

polygon_N10_64 = pya.Polygon([ pya.Point(472, 572), pya.Point(544, 572), pya.Point(544, 644), pya.Point(472, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_64)

polygon_N10_65 = pya.Polygon([ pya.Point(1480, 572), pya.Point(1552, 572), pya.Point(1552, 644), pya.Point(1480, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_65)

polygon_N10_66 = pya.Polygon([ pya.Point(472, 284), pya.Point(544, 284), pya.Point(544, 356), pya.Point(472, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_66)

polygon_N10_67 = pya.Polygon([ pya.Point(1480, 140), pya.Point(1552, 140), pya.Point(1552, 212), pya.Point(1480, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_67)

polygon_N11_68 = pya.Polygon([ pya.Point(760, 428), pya.Point(832, 428), pya.Point(832, 500), pya.Point(760, 500), ])
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


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1704, -64), pya.Point(1704, 1264), pya.Point(16, 1264)]))

layout.write("../gds/Cell7.gds")
