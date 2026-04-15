import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell130")

polygon_N1_0 = pya.Polygon([ pya.Point(304, 1148), pya.Point(1416, 1148), pya.Point(1416, 1220), pya.Point(304, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N10_1 = pya.Polygon([ pya.Point(520, 716), pya.Point(840, 716), pya.Point(840, 788), pya.Point(520, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_1)

polygon_N11_2 = pya.Polygon([ pya.Point(880, 284), pya.Point(1128, 284), pya.Point(1128, 356), pya.Point(880, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_2)

polygon_N11_3 = pya.Polygon([ pya.Point(880, 716), pya.Point(1056, 716), pya.Point(1056, 788), pya.Point(880, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_3)

polygon_N12_4 = pya.Polygon([ pya.Point(1456, 716), pya.Point(1632, 716), pya.Point(1632, 788), pya.Point(1456, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_4)

polygon_N13_5 = pya.Polygon([ pya.Point(1384, 140), pya.Point(1848, 140), pya.Point(1848, 212), pya.Point(1384, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_5)

polygon_N13_6 = pya.Polygon([ pya.Point(1672, 716), pya.Point(1848, 716), pya.Point(1848, 788), pya.Point(1672, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_6)

polygon_N14_7 = pya.Polygon([ pya.Point(1168, 284), pya.Point(1776, 284), pya.Point(1776, 356), pya.Point(1168, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_7)

polygon_N15_8 = pya.Polygon([ pya.Point(664, 140), pya.Point(840, 140), pya.Point(840, 212), pya.Point(664, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N15_8)

polygon_N2_9 = pya.Polygon([ pya.Point(16, 140), pya.Point(408, 140), pya.Point(408, 212), pya.Point(16, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_9)

polygon_N2_10 = pya.Polygon([ pya.Point(304, 716), pya.Point(480, 716), pya.Point(480, 788), pya.Point(304, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_10)

polygon_N2_11 = pya.Polygon([ pya.Point(16, 1004), pya.Point(192, 1004), pya.Point(192, 1076), pya.Point(16, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_11)

polygon_N3_12 = pya.Polygon([ pya.Point(88, -4), pya.Point(696, -4), pya.Point(696, 68), pya.Point(88, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_12)

polygon_N3_13 = pya.Polygon([ pya.Point(88, 716), pya.Point(264, 716), pya.Point(264, 788), pya.Point(88, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_13)

polygon_N3_14 = pya.Polygon([ pya.Point(376, 1004), pya.Point(696, 1004), pya.Point(696, 1076), pya.Point(376, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_14)

polygon_N4_15 = pya.Polygon([ pya.Point(736, -4), pya.Point(1200, -4), pya.Point(1200, 68), pya.Point(736, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_15)

polygon_N4_16 = pya.Polygon([ pya.Point(520, 284), pya.Point(840, 284), pya.Point(840, 356), pya.Point(520, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_16)

polygon_N4_17 = pya.Polygon([ pya.Point(1024, 572), pya.Point(1344, 572), pya.Point(1344, 644), pya.Point(1024, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_17)

polygon_N4_18 = pya.Polygon([ pya.Point(1024, 1004), pya.Point(1200, 1004), pya.Point(1200, 1076), pya.Point(1024, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_18)

polygon_N5_19 = pya.Polygon([ pya.Point(448, 428), pya.Point(1200, 428), pya.Point(1200, 500), pya.Point(448, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_19)

polygon_N5_20 = pya.Polygon([ pya.Point(1240, -4), pya.Point(1416, -4), pya.Point(1416, 68), pya.Point(1240, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_20)

polygon_N5_21 = pya.Polygon([ pya.Point(1096, 716), pya.Point(1416, 716), pya.Point(1416, 788), pya.Point(1096, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_21)

polygon_N5_22 = pya.Polygon([ pya.Point(1240, 1004), pya.Point(1416, 1004), pya.Point(1416, 1076), pya.Point(1240, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_22)

polygon_N6_23 = pya.Polygon([ pya.Point(1672, 1004), pya.Point(1848, 1004), pya.Point(1848, 1076), pya.Point(1672, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_23)

polygon_N7_24 = pya.Polygon([ pya.Point(232, 860), pya.Point(552, 860), pya.Point(552, 932), pya.Point(232, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_24)

polygon_N8_25 = pya.Polygon([ pya.Point(952, 140), pya.Point(1272, 140), pya.Point(1272, 212), pya.Point(952, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_25)

polygon_N8_26 = pya.Polygon([ pya.Point(1168, 860), pya.Point(1344, 860), pya.Point(1344, 932), pya.Point(1168, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_26)

polygon_N9_27 = pya.Polygon([ pya.Point(1312, 428), pya.Point(1704, 428), pya.Point(1704, 500), pya.Point(1312, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_27)

polygon_N9_28 = pya.Polygon([ pya.Point(1528, 860), pya.Point(1704, 860), pya.Point(1704, 932), pya.Point(1528, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_28)

polygon_N10_29 = pya.Polygon([ pya.Point(760, 656), pya.Point(832, 656), pya.Point(832, 832), pya.Point(760, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_29)

polygon_N11_30 = pya.Polygon([ pya.Point(904, 224), pya.Point(976, 224), pya.Point(976, 832), pya.Point(904, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_30)

polygon_N12_31 = pya.Polygon([ pya.Point(1480, 656), pya.Point(1552, 656), pya.Point(1552, 832), pya.Point(1480, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N12_31)

polygon_N13_32 = pya.Polygon([ pya.Point(1768, 80), pya.Point(1840, 80), pya.Point(1840, 832), pya.Point(1768, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N13_32)

polygon_N15_33 = pya.Polygon([ pya.Point(760, 80), pya.Point(832, 80), pya.Point(832, 256), pya.Point(760, 256), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N15_33)

polygon_N2_34 = pya.Polygon([ pya.Point(40, 80), pya.Point(112, 80), pya.Point(112, 1120), pya.Point(40, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_34)

polygon_N2_35 = pya.Polygon([ pya.Point(328, 80), pya.Point(400, 80), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_35)

polygon_N3_36 = pya.Polygon([ pya.Point(184, -64), pya.Point(256, -64), pya.Point(256, 832), pya.Point(184, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_36)

polygon_N3_37 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 1120), pya.Point(616, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_37)

polygon_N4_38 = pya.Polygon([ pya.Point(1048, -64), pya.Point(1120, -64), pya.Point(1120, 1120), pya.Point(1048, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_38)

polygon_N5_39 = pya.Polygon([ pya.Point(1336, -64), pya.Point(1408, -64), pya.Point(1408, 1120), pya.Point(1336, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_39)

polygon_N6_40 = pya.Polygon([ pya.Point(1768, 944), pya.Point(1840, 944), pya.Point(1840, 1120), pya.Point(1768, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_40)

polygon_N7_41 = pya.Polygon([ pya.Point(472, 800), pya.Point(544, 800), pya.Point(544, 976), pya.Point(472, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_41)

polygon_N8_42 = pya.Polygon([ pya.Point(1192, 80), pya.Point(1264, 80), pya.Point(1264, 976), pya.Point(1192, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_42)

polygon_N9_43 = pya.Polygon([ pya.Point(1624, 368), pya.Point(1696, 368), pya.Point(1696, 976), pya.Point(1624, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_43)

polygon_N2_44 = pya.Polygon([ pya.Point(40, 1004), pya.Point(112, 1004), pya.Point(112, 1076), pya.Point(40, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_44)

polygon_N2_45 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_45)

polygon_N2_46 = pya.Polygon([ pya.Point(40, 140), pya.Point(112, 140), pya.Point(112, 212), pya.Point(40, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_46)

polygon_N2_47 = pya.Polygon([ pya.Point(328, 140), pya.Point(400, 140), pya.Point(400, 212), pya.Point(328, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_47)

polygon_N3_48 = pya.Polygon([ pya.Point(616, 1004), pya.Point(688, 1004), pya.Point(688, 1076), pya.Point(616, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_48)

polygon_N3_49 = pya.Polygon([ pya.Point(184, 716), pya.Point(256, 716), pya.Point(256, 788), pya.Point(184, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_49)

polygon_N3_50 = pya.Polygon([ pya.Point(184, -4), pya.Point(256, -4), pya.Point(256, 68), pya.Point(184, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_50)

polygon_N3_51 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_51)

polygon_N4_52 = pya.Polygon([ pya.Point(1048, 1004), pya.Point(1120, 1004), pya.Point(1120, 1076), pya.Point(1048, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_52)

polygon_N4_53 = pya.Polygon([ pya.Point(1048, 572), pya.Point(1120, 572), pya.Point(1120, 644), pya.Point(1048, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_53)

polygon_N4_54 = pya.Polygon([ pya.Point(1048, -4), pya.Point(1120, -4), pya.Point(1120, 68), pya.Point(1048, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_54)

polygon_N5_55 = pya.Polygon([ pya.Point(1336, 1004), pya.Point(1408, 1004), pya.Point(1408, 1076), pya.Point(1336, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_55)

polygon_N5_56 = pya.Polygon([ pya.Point(1336, 716), pya.Point(1408, 716), pya.Point(1408, 788), pya.Point(1336, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_56)

polygon_N5_57 = pya.Polygon([ pya.Point(1336, -4), pya.Point(1408, -4), pya.Point(1408, 68), pya.Point(1336, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_57)

polygon_N6_58 = pya.Polygon([ pya.Point(1768, 1004), pya.Point(1840, 1004), pya.Point(1840, 1076), pya.Point(1768, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_58)

polygon_N7_59 = pya.Polygon([ pya.Point(472, 860), pya.Point(544, 860), pya.Point(544, 932), pya.Point(472, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_59)

polygon_N8_60 = pya.Polygon([ pya.Point(1192, 860), pya.Point(1264, 860), pya.Point(1264, 932), pya.Point(1192, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_60)

polygon_N8_61 = pya.Polygon([ pya.Point(1192, 140), pya.Point(1264, 140), pya.Point(1264, 212), pya.Point(1192, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_61)

polygon_N9_62 = pya.Polygon([ pya.Point(1624, 860), pya.Point(1696, 860), pya.Point(1696, 932), pya.Point(1624, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_62)

polygon_N9_63 = pya.Polygon([ pya.Point(1624, 428), pya.Point(1696, 428), pya.Point(1696, 500), pya.Point(1624, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_63)

polygon_N10_64 = pya.Polygon([ pya.Point(760, 716), pya.Point(832, 716), pya.Point(832, 788), pya.Point(760, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_64)

polygon_N11_65 = pya.Polygon([ pya.Point(904, 716), pya.Point(976, 716), pya.Point(976, 788), pya.Point(904, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_65)

polygon_N11_66 = pya.Polygon([ pya.Point(904, 284), pya.Point(976, 284), pya.Point(976, 356), pya.Point(904, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_66)

polygon_N12_67 = pya.Polygon([ pya.Point(1480, 716), pya.Point(1552, 716), pya.Point(1552, 788), pya.Point(1480, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_67)

polygon_N13_68 = pya.Polygon([ pya.Point(1768, 716), pya.Point(1840, 716), pya.Point(1840, 788), pya.Point(1768, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_68)

polygon_N13_69 = pya.Polygon([ pya.Point(1768, 140), pya.Point(1840, 140), pya.Point(1840, 212), pya.Point(1768, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_69)

polygon_N15_70 = pya.Polygon([ pya.Point(760, 140), pya.Point(832, 140), pya.Point(832, 212), pya.Point(760, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N15_70)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1848, -64), pya.Point(1848, 1220), pya.Point(16, 1220)]))

layout.write("../gds/Cell130.gds")
