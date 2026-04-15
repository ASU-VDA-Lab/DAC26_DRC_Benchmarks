import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell23")

polygon_N1_0 = pya.Polygon([ pya.Point(304, -4), pya.Point(480, -4), pya.Point(480, 68), pya.Point(304, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(304, 716), pya.Point(984, 716), pya.Point(984, 788), pya.Point(304, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N1_2 = pya.Polygon([ pya.Point(304, 1148), pya.Point(480, 1148), pya.Point(480, 1220), pya.Point(304, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_2)

polygon_N10_3 = pya.Polygon([ pya.Point(16, 284), pya.Point(408, 284), pya.Point(408, 356), pya.Point(16, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_3)

polygon_N11_4 = pya.Polygon([ pya.Point(1096, -4), pya.Point(1272, -4), pya.Point(1272, 68), pya.Point(1096, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_4)

polygon_N11_5 = pya.Polygon([ pya.Point(448, 284), pya.Point(840, 284), pya.Point(840, 356), pya.Point(448, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_5)

polygon_N2_6 = pya.Polygon([ pya.Point(448, 140), pya.Point(696, 140), pya.Point(696, 212), pya.Point(448, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_6)

polygon_N2_7 = pya.Polygon([ pya.Point(16, 860), pya.Point(552, 860), pya.Point(552, 932), pya.Point(16, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_7)

polygon_N2_8 = pya.Polygon([ pya.Point(520, 1148), pya.Point(1056, 1148), pya.Point(1056, 1220), pya.Point(520, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_8)

polygon_N3_9 = pya.Polygon([ pya.Point(1096, 1148), pya.Point(1272, 1148), pya.Point(1272, 1220), pya.Point(1096, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_9)

polygon_N4_10 = pya.Polygon([ pya.Point(160, 1004), pya.Point(336, 1004), pya.Point(336, 1076), pya.Point(160, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_10)

polygon_N5_11 = pya.Polygon([ pya.Point(448, 1004), pya.Point(1128, 1004), pya.Point(1128, 1076), pya.Point(448, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_11)

polygon_N5_12 = pya.Polygon([ pya.Point(808, 140), pya.Point(1128, 140), pya.Point(1128, 212), pya.Point(808, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_12)

polygon_N6_13 = pya.Polygon([ pya.Point(592, -4), pya.Point(984, -4), pya.Point(984, 68), pya.Point(592, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_13)

polygon_N6_14 = pya.Polygon([ pya.Point(880, 284), pya.Point(1056, 284), pya.Point(1056, 356), pya.Point(880, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_14)

polygon_N6_15 = pya.Polygon([ pya.Point(664, 860), pya.Point(984, 860), pya.Point(984, 932), pya.Point(664, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_15)

polygon_N7_16 = pya.Polygon([ pya.Point(16, 716), pya.Point(192, 716), pya.Point(192, 788), pya.Point(16, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_16)

polygon_N8_17 = pya.Polygon([ pya.Point(88, -4), pya.Point(264, -4), pya.Point(264, 68), pya.Point(88, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_17)

polygon_N8_18 = pya.Polygon([ pya.Point(160, 572), pya.Point(1272, 572), pya.Point(1272, 644), pya.Point(160, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_18)

polygon_N8_19 = pya.Polygon([ pya.Point(1096, 284), pya.Point(1272, 284), pya.Point(1272, 356), pya.Point(1096, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_19)

polygon_N8_20 = pya.Polygon([ pya.Point(1096, 716), pya.Point(1272, 716), pya.Point(1272, 788), pya.Point(1096, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_20)

polygon_N9_21 = pya.Polygon([ pya.Point(16, 140), pya.Point(336, 140), pya.Point(336, 212), pya.Point(16, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_21)

polygon_N9_22 = pya.Polygon([ pya.Point(232, 428), pya.Point(1056, 428), pya.Point(1056, 500), pya.Point(232, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_22)

polygon_N1_23 = pya.Polygon([ pya.Point(328, -64), pya.Point(400, -64), pya.Point(400, 1264), pya.Point(328, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_23)

polygon_N11_24 = pya.Polygon([ pya.Point(760, -64), pya.Point(832, -64), pya.Point(832, 400), pya.Point(760, 400), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_24)

polygon_N11_25 = pya.Polygon([ pya.Point(1192, -64), pya.Point(1264, -64), pya.Point(1264, 112), pya.Point(1192, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_25)

polygon_N2_26 = pya.Polygon([ pya.Point(472, 80), pya.Point(544, 80), pya.Point(544, 976), pya.Point(472, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_26)

polygon_N2_27 = pya.Polygon([ pya.Point(616, 80), pya.Point(688, 80), pya.Point(688, 1264), pya.Point(616, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_27)

polygon_N3_28 = pya.Polygon([ pya.Point(1192, 1088), pya.Point(1264, 1088), pya.Point(1264, 1264), pya.Point(1192, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_28)

polygon_N4_29 = pya.Polygon([ pya.Point(184, 944), pya.Point(256, 944), pya.Point(256, 1120), pya.Point(184, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_29)

polygon_N5_30 = pya.Polygon([ pya.Point(1048, 80), pya.Point(1120, 80), pya.Point(1120, 1120), pya.Point(1048, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_30)

polygon_N6_31 = pya.Polygon([ pya.Point(904, -64), pya.Point(976, -64), pya.Point(976, 976), pya.Point(904, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_31)

polygon_N7_32 = pya.Polygon([ pya.Point(40, 656), pya.Point(112, 656), pya.Point(112, 832), pya.Point(40, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_32)

polygon_N8_33 = pya.Polygon([ pya.Point(184, -64), pya.Point(256, -64), pya.Point(256, 688), pya.Point(184, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_33)

polygon_N8_34 = pya.Polygon([ pya.Point(1192, 224), pya.Point(1264, 224), pya.Point(1264, 832), pya.Point(1192, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_34)

polygon_N9_35 = pya.Polygon([ pya.Point(40, 80), pya.Point(112, 80), pya.Point(112, 256), pya.Point(40, 256), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_35)

polygon_N11_36 = pya.Polygon([ pya.Point(704, -4), pya.Point(1392, -4), pya.Point(1392, 68), pya.Point(704, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(20, 0))).insert(polygon_N11_36)

polygon_N1_37 = pya.Polygon([ pya.Point(328, 1148), pya.Point(400, 1148), pya.Point(400, 1220), pya.Point(328, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_37)

polygon_N1_38 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_38)

polygon_N1_39 = pya.Polygon([ pya.Point(328, -4), pya.Point(400, -4), pya.Point(400, 68), pya.Point(328, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_39)

polygon_N2_40 = pya.Polygon([ pya.Point(616, 1148), pya.Point(688, 1148), pya.Point(688, 1220), pya.Point(616, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_40)

polygon_N2_41 = pya.Polygon([ pya.Point(472, 860), pya.Point(544, 860), pya.Point(544, 932), pya.Point(472, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_41)

polygon_N2_42 = pya.Polygon([ pya.Point(472, 140), pya.Point(544, 140), pya.Point(544, 212), pya.Point(472, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_42)

polygon_N2_43 = pya.Polygon([ pya.Point(616, 140), pya.Point(688, 140), pya.Point(688, 212), pya.Point(616, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_43)

polygon_N3_44 = pya.Polygon([ pya.Point(1192, 1148), pya.Point(1264, 1148), pya.Point(1264, 1220), pya.Point(1192, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_44)

polygon_N4_45 = pya.Polygon([ pya.Point(184, 1004), pya.Point(256, 1004), pya.Point(256, 1076), pya.Point(184, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_45)

polygon_N5_46 = pya.Polygon([ pya.Point(1048, 1004), pya.Point(1120, 1004), pya.Point(1120, 1076), pya.Point(1048, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_46)

polygon_N5_47 = pya.Polygon([ pya.Point(1048, 140), pya.Point(1120, 140), pya.Point(1120, 212), pya.Point(1048, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_47)

polygon_N6_48 = pya.Polygon([ pya.Point(904, 860), pya.Point(976, 860), pya.Point(976, 932), pya.Point(904, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_48)

polygon_N6_49 = pya.Polygon([ pya.Point(904, 284), pya.Point(976, 284), pya.Point(976, 356), pya.Point(904, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_49)

polygon_N6_50 = pya.Polygon([ pya.Point(904, -4), pya.Point(976, -4), pya.Point(976, 68), pya.Point(904, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_50)

polygon_N7_51 = pya.Polygon([ pya.Point(40, 716), pya.Point(112, 716), pya.Point(112, 788), pya.Point(40, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_51)

polygon_N8_52 = pya.Polygon([ pya.Point(1192, 716), pya.Point(1264, 716), pya.Point(1264, 788), pya.Point(1192, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_52)

polygon_N8_53 = pya.Polygon([ pya.Point(184, 572), pya.Point(256, 572), pya.Point(256, 644), pya.Point(184, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_53)

polygon_N8_54 = pya.Polygon([ pya.Point(1192, 572), pya.Point(1264, 572), pya.Point(1264, 644), pya.Point(1192, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_54)

polygon_N8_55 = pya.Polygon([ pya.Point(1192, 284), pya.Point(1264, 284), pya.Point(1264, 356), pya.Point(1192, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_55)

polygon_N8_56 = pya.Polygon([ pya.Point(184, -4), pya.Point(256, -4), pya.Point(256, 68), pya.Point(184, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_56)

polygon_N9_57 = pya.Polygon([ pya.Point(40, 140), pya.Point(112, 140), pya.Point(112, 212), pya.Point(40, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_57)

polygon_N11_58 = pya.Polygon([ pya.Point(760, 284), pya.Point(832, 284), pya.Point(832, 356), pya.Point(760, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_58)

polygon_N11_59 = pya.Polygon([ pya.Point(1192, -4), pya.Point(1264, -4), pya.Point(1264, 68), pya.Point(1192, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_59)

polygon_N11_60 = pya.Polygon([ pya.Point(760, -4), pya.Point(832, -4), pya.Point(832, 68), pya.Point(760, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(21, 0))).insert(polygon_N11_60)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1392, -64), pya.Point(1392, 1264), pya.Point(16, 1264)]))

layout.write("../gds/Cell23.gds")
