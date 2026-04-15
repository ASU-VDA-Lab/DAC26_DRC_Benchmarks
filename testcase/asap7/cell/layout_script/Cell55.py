import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell55")

polygon_N1_0 = pya.Polygon([ pya.Point(448, 140), pya.Point(1488, 140), pya.Point(1488, 212), pya.Point(448, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(448, 1148), pya.Point(1200, 1148), pya.Point(1200, 1220), pya.Point(448, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N1_2 = pya.Polygon([ pya.Point(880, 572), pya.Point(1056, 572), pya.Point(1056, 644), pya.Point(880, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_2)

polygon_N10_3 = pya.Polygon([ pya.Point(16, 140), pya.Point(336, 140), pya.Point(336, 212), pya.Point(16, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_3)

polygon_N10_4 = pya.Polygon([ pya.Point(16, 716), pya.Point(192, 716), pya.Point(192, 788), pya.Point(16, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_4)

polygon_N11_5 = pya.Polygon([ pya.Point(1024, 716), pya.Point(1488, 716), pya.Point(1488, 788), pya.Point(1024, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_5)

polygon_N12_6 = pya.Polygon([ pya.Point(664, 428), pya.Point(1128, 428), pya.Point(1128, 500), pya.Point(664, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_6)

polygon_N13_7 = pya.Polygon([ pya.Point(520, -4), pya.Point(696, -4), pya.Point(696, 68), pya.Point(520, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_7)

polygon_N2_8 = pya.Polygon([ pya.Point(736, -4), pya.Point(912, -4), pya.Point(912, 68), pya.Point(736, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_8)

polygon_N2_9 = pya.Polygon([ pya.Point(1240, 1148), pya.Point(1416, 1148), pya.Point(1416, 1220), pya.Point(1240, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_9)

polygon_N3_10 = pya.Polygon([ pya.Point(160, 284), pya.Point(696, 284), pya.Point(696, 356), pya.Point(160, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_10)

polygon_N3_11 = pya.Polygon([ pya.Point(160, 1004), pya.Point(480, 1004), pya.Point(480, 1076), pya.Point(160, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_11)

polygon_N3_12 = pya.Polygon([ pya.Point(592, 716), pya.Point(984, 716), pya.Point(984, 788), pya.Point(592, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_12)

polygon_N4_13 = pya.Polygon([ pya.Point(520, 1004), pya.Point(696, 1004), pya.Point(696, 1076), pya.Point(520, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_13)

polygon_N5_14 = pya.Polygon([ pya.Point(304, -4), pya.Point(480, -4), pya.Point(480, 68), pya.Point(304, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_14)

polygon_N5_15 = pya.Polygon([ pya.Point(304, 572), pya.Point(840, 572), pya.Point(840, 644), pya.Point(304, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_15)

polygon_N5_16 = pya.Polygon([ pya.Point(232, 716), pya.Point(480, 716), pya.Point(480, 788), pya.Point(232, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_16)

polygon_N5_17 = pya.Polygon([ pya.Point(736, 1004), pya.Point(912, 1004), pya.Point(912, 1076), pya.Point(736, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_17)

polygon_N6_18 = pya.Polygon([ pya.Point(952, -4), pya.Point(1560, -4), pya.Point(1560, 68), pya.Point(952, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_18)

polygon_N6_19 = pya.Polygon([ pya.Point(1096, 572), pya.Point(1560, 572), pya.Point(1560, 644), pya.Point(1096, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_19)

polygon_N6_20 = pya.Polygon([ pya.Point(952, 1004), pya.Point(1128, 1004), pya.Point(1128, 1076), pya.Point(952, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_20)

polygon_N7_21 = pya.Polygon([ pya.Point(880, 284), pya.Point(1344, 284), pya.Point(1344, 356), pya.Point(880, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_21)

polygon_N7_22 = pya.Polygon([ pya.Point(1168, 1004), pya.Point(1344, 1004), pya.Point(1344, 1076), pya.Point(1168, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_22)

polygon_N8_23 = pya.Polygon([ pya.Point(304, 428), pya.Point(552, 428), pya.Point(552, 500), pya.Point(304, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_23)

polygon_N8_24 = pya.Polygon([ pya.Point(16, 860), pya.Point(552, 860), pya.Point(552, 932), pya.Point(16, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_24)

polygon_N9_25 = pya.Polygon([ pya.Point(664, 860), pya.Point(1560, 860), pya.Point(1560, 932), pya.Point(664, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_25)

polygon_N1_26 = pya.Polygon([ pya.Point(904, 80), pya.Point(976, 80), pya.Point(976, 1264), pya.Point(904, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_26)

polygon_N10_27 = pya.Polygon([ pya.Point(40, 80), pya.Point(112, 80), pya.Point(112, 832), pya.Point(40, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_27)

polygon_N13_28 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 112), pya.Point(616, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N13_28)

polygon_N2_29 = pya.Polygon([ pya.Point(760, -64), pya.Point(832, -64), pya.Point(832, 112), pya.Point(760, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_29)

polygon_N2_30 = pya.Polygon([ pya.Point(1336, -64), pya.Point(1408, -64), pya.Point(1408, 1264), pya.Point(1336, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_30)

polygon_N3_31 = pya.Polygon([ pya.Point(184, 224), pya.Point(256, 224), pya.Point(256, 1120), pya.Point(184, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_31)

polygon_N3_32 = pya.Polygon([ pya.Point(616, 224), pya.Point(688, 224), pya.Point(688, 832), pya.Point(616, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_32)

polygon_N4_33 = pya.Polygon([ pya.Point(616, 944), pya.Point(688, 944), pya.Point(688, 1120), pya.Point(616, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_33)

polygon_N5_34 = pya.Polygon([ pya.Point(328, -64), pya.Point(400, -64), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_34)

polygon_N5_35 = pya.Polygon([ pya.Point(760, 512), pya.Point(832, 512), pya.Point(832, 1120), pya.Point(760, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_35)

polygon_N6_36 = pya.Polygon([ pya.Point(1048, -64), pya.Point(1120, -64), pya.Point(1120, 1120), pya.Point(1048, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_36)

polygon_N6_37 = pya.Polygon([ pya.Point(1480, -64), pya.Point(1552, -64), pya.Point(1552, 688), pya.Point(1480, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_37)

polygon_N7_38 = pya.Polygon([ pya.Point(1192, 224), pya.Point(1264, 224), pya.Point(1264, 1120), pya.Point(1192, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_38)

polygon_N8_39 = pya.Polygon([ pya.Point(472, 368), pya.Point(544, 368), pya.Point(544, 976), pya.Point(472, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_39)

polygon_N2_40 = pya.Polygon([ pya.Point(704, -4), pya.Point(1536, -4), pya.Point(1536, 68), pya.Point(704, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(20, 0))).insert(polygon_N2_40)

polygon_N1_41 = pya.Polygon([ pya.Point(904, 1148), pya.Point(976, 1148), pya.Point(976, 1220), pya.Point(904, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_41)

polygon_N1_42 = pya.Polygon([ pya.Point(904, 572), pya.Point(976, 572), pya.Point(976, 644), pya.Point(904, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_42)

polygon_N1_43 = pya.Polygon([ pya.Point(904, 140), pya.Point(976, 140), pya.Point(976, 212), pya.Point(904, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_43)

polygon_N2_44 = pya.Polygon([ pya.Point(1336, 1148), pya.Point(1408, 1148), pya.Point(1408, 1220), pya.Point(1336, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_44)

polygon_N2_45 = pya.Polygon([ pya.Point(760, -4), pya.Point(832, -4), pya.Point(832, 68), pya.Point(760, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_45)

polygon_N3_46 = pya.Polygon([ pya.Point(184, 1004), pya.Point(256, 1004), pya.Point(256, 1076), pya.Point(184, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_46)

polygon_N3_47 = pya.Polygon([ pya.Point(616, 716), pya.Point(688, 716), pya.Point(688, 788), pya.Point(616, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_47)

polygon_N3_48 = pya.Polygon([ pya.Point(184, 284), pya.Point(256, 284), pya.Point(256, 356), pya.Point(184, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_48)

polygon_N3_49 = pya.Polygon([ pya.Point(616, 284), pya.Point(688, 284), pya.Point(688, 356), pya.Point(616, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_49)

polygon_N4_50 = pya.Polygon([ pya.Point(616, 1004), pya.Point(688, 1004), pya.Point(688, 1076), pya.Point(616, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_50)

polygon_N5_51 = pya.Polygon([ pya.Point(760, 1004), pya.Point(832, 1004), pya.Point(832, 1076), pya.Point(760, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_51)

polygon_N5_52 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_52)

polygon_N5_53 = pya.Polygon([ pya.Point(328, 572), pya.Point(400, 572), pya.Point(400, 644), pya.Point(328, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_53)

polygon_N5_54 = pya.Polygon([ pya.Point(760, 572), pya.Point(832, 572), pya.Point(832, 644), pya.Point(760, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_54)

polygon_N5_55 = pya.Polygon([ pya.Point(328, -4), pya.Point(400, -4), pya.Point(400, 68), pya.Point(328, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_55)

polygon_N6_56 = pya.Polygon([ pya.Point(1048, 1004), pya.Point(1120, 1004), pya.Point(1120, 1076), pya.Point(1048, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_56)

polygon_N6_57 = pya.Polygon([ pya.Point(1480, 572), pya.Point(1552, 572), pya.Point(1552, 644), pya.Point(1480, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_57)

polygon_N6_58 = pya.Polygon([ pya.Point(1048, -4), pya.Point(1120, -4), pya.Point(1120, 68), pya.Point(1048, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_58)

polygon_N6_59 = pya.Polygon([ pya.Point(1480, -4), pya.Point(1552, -4), pya.Point(1552, 68), pya.Point(1480, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_59)

polygon_N7_60 = pya.Polygon([ pya.Point(1192, 1004), pya.Point(1264, 1004), pya.Point(1264, 1076), pya.Point(1192, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_60)

polygon_N7_61 = pya.Polygon([ pya.Point(1192, 284), pya.Point(1264, 284), pya.Point(1264, 356), pya.Point(1192, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_61)

polygon_N8_62 = pya.Polygon([ pya.Point(472, 860), pya.Point(544, 860), pya.Point(544, 932), pya.Point(472, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_62)

polygon_N8_63 = pya.Polygon([ pya.Point(472, 428), pya.Point(544, 428), pya.Point(544, 500), pya.Point(472, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_63)

polygon_N10_64 = pya.Polygon([ pya.Point(40, 716), pya.Point(112, 716), pya.Point(112, 788), pya.Point(40, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_64)

polygon_N10_65 = pya.Polygon([ pya.Point(40, 140), pya.Point(112, 140), pya.Point(112, 212), pya.Point(40, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_65)

polygon_N13_66 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_66)

polygon_N2_67 = pya.Polygon([ pya.Point(1336, -4), pya.Point(1408, -4), pya.Point(1408, 68), pya.Point(1336, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(21, 0))).insert(polygon_N2_67)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1560, -64), pya.Point(1560, 1264), pya.Point(16, 1264)]))

layout.write("../gds/Cell55.gds")
