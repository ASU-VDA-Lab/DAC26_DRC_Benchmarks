import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell213")

polygon_N1_0 = pya.Polygon([ pya.Point(304, 1148), pya.Point(1776, 1148), pya.Point(1776, 1220), pya.Point(304, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N10_1 = pya.Polygon([ pya.Point(448, 716), pya.Point(984, 716), pya.Point(984, 788), pya.Point(448, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_1)

polygon_N11_2 = pya.Polygon([ pya.Point(1024, 428), pya.Point(1200, 428), pya.Point(1200, 500), pya.Point(1024, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_2)

polygon_N11_3 = pya.Polygon([ pya.Point(1024, 716), pya.Point(1344, 716), pya.Point(1344, 788), pya.Point(1024, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_3)

polygon_N12_4 = pya.Polygon([ pya.Point(1672, 716), pya.Point(1848, 716), pya.Point(1848, 788), pya.Point(1672, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_4)

polygon_N13_5 = pya.Polygon([ pya.Point(304, 428), pya.Point(984, 428), pya.Point(984, 500), pya.Point(304, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_5)

polygon_N14_6 = pya.Polygon([ pya.Point(592, -4), pya.Point(768, -4), pya.Point(768, 68), pya.Point(592, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_6)

polygon_N14_7 = pya.Polygon([ pya.Point(520, 284), pya.Point(768, 284), pya.Point(768, 356), pya.Point(520, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_7)

polygon_N15_8 = pya.Polygon([ pya.Point(304, 140), pya.Point(984, 140), pya.Point(984, 212), pya.Point(304, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N15_8)

polygon_N16_9 = pya.Polygon([ pya.Point(160, -4), pya.Point(336, -4), pya.Point(336, 68), pya.Point(160, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N16_9)

polygon_N17_10 = pya.Polygon([ pya.Point(1672, -4), pya.Point(1848, -4), pya.Point(1848, 68), pya.Point(1672, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N17_10)

polygon_N2_11 = pya.Polygon([ pya.Point(1024, 140), pya.Point(1704, 140), pya.Point(1704, 212), pya.Point(1024, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_11)

polygon_N2_12 = pya.Polygon([ pya.Point(664, 1004), pya.Point(840, 1004), pya.Point(840, 1076), pya.Point(664, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_12)

polygon_N2_13 = pya.Polygon([ pya.Point(1528, 860), pya.Point(1776, 860), pya.Point(1776, 932), pya.Point(1528, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_13)

polygon_N3_14 = pya.Polygon([ pya.Point(880, -4), pya.Point(1056, -4), pya.Point(1056, 68), pya.Point(880, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_14)

polygon_N3_15 = pya.Polygon([ pya.Point(880, 284), pya.Point(1848, 284), pya.Point(1848, 356), pya.Point(880, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_15)

polygon_N3_16 = pya.Polygon([ pya.Point(880, 1004), pya.Point(1056, 1004), pya.Point(1056, 1076), pya.Point(880, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_16)

polygon_N4_17 = pya.Polygon([ pya.Point(1096, -4), pya.Point(1632, -4), pya.Point(1632, 68), pya.Point(1096, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_17)

polygon_N4_18 = pya.Polygon([ pya.Point(952, 572), pya.Point(1272, 572), pya.Point(1272, 644), pya.Point(952, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_18)

polygon_N4_19 = pya.Polygon([ pya.Point(1096, 1004), pya.Point(1272, 1004), pya.Point(1272, 1076), pya.Point(1096, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_19)

polygon_N5_20 = pya.Polygon([ pya.Point(1312, 1004), pya.Point(1560, 1004), pya.Point(1560, 1076), pya.Point(1312, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_20)

polygon_N6_21 = pya.Polygon([ pya.Point(16, 140), pya.Point(264, 140), pya.Point(264, 212), pya.Point(16, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_21)

polygon_N6_22 = pya.Polygon([ pya.Point(16, 284), pya.Point(480, 284), pya.Point(480, 356), pya.Point(16, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_22)

polygon_N6_23 = pya.Polygon([ pya.Point(16, 860), pya.Point(192, 860), pya.Point(192, 932), pya.Point(16, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_23)

polygon_N7_24 = pya.Polygon([ pya.Point(232, 860), pya.Point(1128, 860), pya.Point(1128, 932), pya.Point(232, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_24)

polygon_N8_25 = pya.Polygon([ pya.Point(1240, 428), pya.Point(1560, 428), pya.Point(1560, 500), pya.Point(1240, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_25)

polygon_N8_26 = pya.Polygon([ pya.Point(1456, 716), pya.Point(1632, 716), pya.Point(1632, 788), pya.Point(1456, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_26)

polygon_N8_27 = pya.Polygon([ pya.Point(1168, 860), pya.Point(1416, 860), pya.Point(1416, 932), pya.Point(1168, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_27)

polygon_N9_28 = pya.Polygon([ pya.Point(376, -4), pya.Point(552, -4), pya.Point(552, 68), pya.Point(376, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_28)

polygon_N9_29 = pya.Polygon([ pya.Point(88, 428), pya.Point(264, 428), pya.Point(264, 500), pya.Point(88, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_29)

polygon_N9_30 = pya.Polygon([ pya.Point(304, 572), pya.Point(552, 572), pya.Point(552, 644), pya.Point(304, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_30)

polygon_N9_31 = pya.Polygon([ pya.Point(88, 716), pya.Point(408, 716), pya.Point(408, 788), pya.Point(88, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_31)

polygon_N11_32 = pya.Polygon([ pya.Point(1048, 368), pya.Point(1120, 368), pya.Point(1120, 832), pya.Point(1048, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_32)

polygon_N12_33 = pya.Polygon([ pya.Point(1768, 656), pya.Point(1840, 656), pya.Point(1840, 832), pya.Point(1768, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N12_33)

polygon_N14_34 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 112), pya.Point(616, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N14_34)

polygon_N16_35 = pya.Polygon([ pya.Point(184, -64), pya.Point(256, -64), pya.Point(256, 112), pya.Point(184, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N16_35)

polygon_N17_36 = pya.Polygon([ pya.Point(1768, -64), pya.Point(1840, -64), pya.Point(1840, 112), pya.Point(1768, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N17_36)

polygon_N2_37 = pya.Polygon([ pya.Point(760, -64), pya.Point(832, -64), pya.Point(832, 1120), pya.Point(760, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_37)

polygon_N2_38 = pya.Polygon([ pya.Point(1048, -64), pya.Point(1120, -64), pya.Point(1120, 256), pya.Point(1048, 256), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_38)

polygon_N2_39 = pya.Polygon([ pya.Point(1624, 80), pya.Point(1696, 80), pya.Point(1696, 976), pya.Point(1624, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_39)

polygon_N3_40 = pya.Polygon([ pya.Point(904, -64), pya.Point(976, -64), pya.Point(976, 1120), pya.Point(904, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_40)

polygon_N4_41 = pya.Polygon([ pya.Point(1192, -64), pya.Point(1264, -64), pya.Point(1264, 1120), pya.Point(1192, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_41)

polygon_N6_42 = pya.Polygon([ pya.Point(40, 80), pya.Point(112, 80), pya.Point(112, 976), pya.Point(40, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_42)

polygon_N8_43 = pya.Polygon([ pya.Point(1336, 368), pya.Point(1408, 368), pya.Point(1408, 976), pya.Point(1336, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_43)

polygon_N8_44 = pya.Polygon([ pya.Point(1480, 368), pya.Point(1552, 368), pya.Point(1552, 832), pya.Point(1480, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_44)

polygon_N9_45 = pya.Polygon([ pya.Point(472, -64), pya.Point(544, -64), pya.Point(544, 688), pya.Point(472, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_45)

polygon_N9_46 = pya.Polygon([ pya.Point(184, 368), pya.Point(256, 368), pya.Point(256, 832), pya.Point(184, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_46)

polygon_N9_47 = pya.Polygon([ pya.Point(328, 512), pya.Point(400, 512), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_47)

polygon_N2_48 = pya.Polygon([ pya.Point(704, -4), pya.Point(1248, -4), pya.Point(1248, 68), pya.Point(704, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(20, 0))).insert(polygon_N2_48)

polygon_N2_49 = pya.Polygon([ pya.Point(760, 1004), pya.Point(832, 1004), pya.Point(832, 1076), pya.Point(760, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_49)

polygon_N2_50 = pya.Polygon([ pya.Point(1624, 860), pya.Point(1696, 860), pya.Point(1696, 932), pya.Point(1624, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_50)

polygon_N2_51 = pya.Polygon([ pya.Point(1048, 140), pya.Point(1120, 140), pya.Point(1120, 212), pya.Point(1048, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_51)

polygon_N2_52 = pya.Polygon([ pya.Point(1624, 140), pya.Point(1696, 140), pya.Point(1696, 212), pya.Point(1624, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_52)

polygon_N3_53 = pya.Polygon([ pya.Point(904, 1004), pya.Point(976, 1004), pya.Point(976, 1076), pya.Point(904, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_53)

polygon_N3_54 = pya.Polygon([ pya.Point(904, 284), pya.Point(976, 284), pya.Point(976, 356), pya.Point(904, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_54)

polygon_N3_55 = pya.Polygon([ pya.Point(904, -4), pya.Point(976, -4), pya.Point(976, 68), pya.Point(904, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_55)

polygon_N4_56 = pya.Polygon([ pya.Point(1192, 1004), pya.Point(1264, 1004), pya.Point(1264, 1076), pya.Point(1192, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_56)

polygon_N4_57 = pya.Polygon([ pya.Point(1192, 572), pya.Point(1264, 572), pya.Point(1264, 644), pya.Point(1192, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_57)

polygon_N4_58 = pya.Polygon([ pya.Point(1192, -4), pya.Point(1264, -4), pya.Point(1264, 68), pya.Point(1192, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_58)

polygon_N6_59 = pya.Polygon([ pya.Point(40, 860), pya.Point(112, 860), pya.Point(112, 932), pya.Point(40, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_59)

polygon_N6_60 = pya.Polygon([ pya.Point(40, 284), pya.Point(112, 284), pya.Point(112, 356), pya.Point(40, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_60)

polygon_N6_61 = pya.Polygon([ pya.Point(40, 140), pya.Point(112, 140), pya.Point(112, 212), pya.Point(40, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_61)

polygon_N8_62 = pya.Polygon([ pya.Point(1336, 860), pya.Point(1408, 860), pya.Point(1408, 932), pya.Point(1336, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_62)

polygon_N8_63 = pya.Polygon([ pya.Point(1480, 716), pya.Point(1552, 716), pya.Point(1552, 788), pya.Point(1480, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_63)

polygon_N8_64 = pya.Polygon([ pya.Point(1336, 428), pya.Point(1408, 428), pya.Point(1408, 500), pya.Point(1336, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_64)

polygon_N8_65 = pya.Polygon([ pya.Point(1480, 428), pya.Point(1552, 428), pya.Point(1552, 500), pya.Point(1480, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_65)

polygon_N9_66 = pya.Polygon([ pya.Point(184, 716), pya.Point(256, 716), pya.Point(256, 788), pya.Point(184, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_66)

polygon_N9_67 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_67)

polygon_N9_68 = pya.Polygon([ pya.Point(328, 572), pya.Point(400, 572), pya.Point(400, 644), pya.Point(328, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_68)

polygon_N9_69 = pya.Polygon([ pya.Point(472, 572), pya.Point(544, 572), pya.Point(544, 644), pya.Point(472, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_69)

polygon_N9_70 = pya.Polygon([ pya.Point(184, 428), pya.Point(256, 428), pya.Point(256, 500), pya.Point(184, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_70)

polygon_N9_71 = pya.Polygon([ pya.Point(472, -4), pya.Point(544, -4), pya.Point(544, 68), pya.Point(472, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_71)

polygon_N11_72 = pya.Polygon([ pya.Point(1048, 716), pya.Point(1120, 716), pya.Point(1120, 788), pya.Point(1048, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_72)

polygon_N11_73 = pya.Polygon([ pya.Point(1048, 428), pya.Point(1120, 428), pya.Point(1120, 500), pya.Point(1048, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_73)

polygon_N12_74 = pya.Polygon([ pya.Point(1768, 716), pya.Point(1840, 716), pya.Point(1840, 788), pya.Point(1768, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_74)

polygon_N14_75 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N14_75)

polygon_N16_76 = pya.Polygon([ pya.Point(184, -4), pya.Point(256, -4), pya.Point(256, 68), pya.Point(184, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N16_76)

polygon_N17_77 = pya.Polygon([ pya.Point(1768, -4), pya.Point(1840, -4), pya.Point(1840, 68), pya.Point(1768, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N17_77)

polygon_N2_78 = pya.Polygon([ pya.Point(760, -4), pya.Point(832, -4), pya.Point(832, 68), pya.Point(760, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(21, 0))).insert(polygon_N2_78)

polygon_N2_79 = pya.Polygon([ pya.Point(1048, -4), pya.Point(1120, -4), pya.Point(1120, 68), pya.Point(1048, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(21, 0))).insert(polygon_N2_79)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1848, -64), pya.Point(1848, 1220), pya.Point(16, 1220)]))

layout.write("../gds/Cell213.gds")
