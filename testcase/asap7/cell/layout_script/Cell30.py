import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell30")

polygon_N1_0 = pya.Polygon([ pya.Point(304, 140), pya.Point(480, 140), pya.Point(480, 212), pya.Point(304, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(304, 284), pya.Point(624, 284), pya.Point(624, 356), pya.Point(304, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N1_2 = pya.Polygon([ pya.Point(304, 1148), pya.Point(984, 1148), pya.Point(984, 1220), pya.Point(304, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_2)

polygon_N10_3 = pya.Polygon([ pya.Point(16, 428), pya.Point(408, 428), pya.Point(408, 500), pya.Point(16, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_3)

polygon_N11_4 = pya.Polygon([ pya.Point(448, 428), pya.Point(1200, 428), pya.Point(1200, 500), pya.Point(448, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_4)

polygon_N2_5 = pya.Polygon([ pya.Point(16, 1004), pya.Point(264, 1004), pya.Point(264, 1076), pya.Point(16, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_5)

polygon_N3_6 = pya.Polygon([ pya.Point(448, -4), pya.Point(696, -4), pya.Point(696, 68), pya.Point(448, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_6)

polygon_N3_7 = pya.Polygon([ pya.Point(16, 860), pya.Point(552, 860), pya.Point(552, 932), pya.Point(16, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_7)

polygon_N3_8 = pya.Polygon([ pya.Point(520, 1004), pya.Point(1056, 1004), pya.Point(1056, 1076), pya.Point(520, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_8)

polygon_N4_9 = pya.Polygon([ pya.Point(1096, 1004), pya.Point(1272, 1004), pya.Point(1272, 1076), pya.Point(1096, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_9)

polygon_N5_10 = pya.Polygon([ pya.Point(592, 140), pya.Point(984, 140), pya.Point(984, 212), pya.Point(592, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_10)

polygon_N5_11 = pya.Polygon([ pya.Point(880, 284), pya.Point(1128, 284), pya.Point(1128, 356), pya.Point(880, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_11)

polygon_N5_12 = pya.Polygon([ pya.Point(664, 860), pya.Point(984, 860), pya.Point(984, 932), pya.Point(664, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_12)

polygon_N6_13 = pya.Polygon([ pya.Point(160, 716), pya.Point(336, 716), pya.Point(336, 788), pya.Point(160, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_13)

polygon_N7_14 = pya.Polygon([ pya.Point(736, -4), pya.Point(912, -4), pya.Point(912, 68), pya.Point(736, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_14)

polygon_N7_15 = pya.Polygon([ pya.Point(376, 716), pya.Point(840, 716), pya.Point(840, 788), pya.Point(376, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_15)

polygon_N8_16 = pya.Polygon([ pya.Point(88, 140), pya.Point(264, 140), pya.Point(264, 212), pya.Point(88, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_16)

polygon_N8_17 = pya.Polygon([ pya.Point(1024, 140), pya.Point(1272, 140), pya.Point(1272, 212), pya.Point(1024, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_17)

polygon_N8_18 = pya.Polygon([ pya.Point(1024, 716), pya.Point(1272, 716), pya.Point(1272, 788), pya.Point(1024, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_18)

polygon_N9_19 = pya.Polygon([ pya.Point(16, -4), pya.Point(336, -4), pya.Point(336, 68), pya.Point(16, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_19)

polygon_N9_20 = pya.Polygon([ pya.Point(16, 572), pya.Point(1272, 572), pya.Point(1272, 644), pya.Point(16, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_20)

polygon_N9_21 = pya.Polygon([ pya.Point(952, -4), pya.Point(1272, -4), pya.Point(1272, 68), pya.Point(952, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_21)

polygon_N1_22 = pya.Polygon([ pya.Point(328, 80), pya.Point(400, 80), pya.Point(400, 1264), pya.Point(328, 1264), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_22)

polygon_N2_23 = pya.Polygon([ pya.Point(40, 944), pya.Point(112, 944), pya.Point(112, 1120), pya.Point(40, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_23)

polygon_N3_24 = pya.Polygon([ pya.Point(472, -64), pya.Point(544, -64), pya.Point(544, 976), pya.Point(472, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_24)

polygon_N3_25 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 1120), pya.Point(616, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_25)

polygon_N4_26 = pya.Polygon([ pya.Point(1192, 944), pya.Point(1264, 944), pya.Point(1264, 1120), pya.Point(1192, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_26)

polygon_N5_27 = pya.Polygon([ pya.Point(904, 80), pya.Point(976, 80), pya.Point(976, 976), pya.Point(904, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_27)

polygon_N6_28 = pya.Polygon([ pya.Point(184, 656), pya.Point(256, 656), pya.Point(256, 832), pya.Point(184, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_28)

polygon_N7_29 = pya.Polygon([ pya.Point(760, -64), pya.Point(832, -64), pya.Point(832, 832), pya.Point(760, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_29)

polygon_N8_30 = pya.Polygon([ pya.Point(184, 80), pya.Point(256, 80), pya.Point(256, 256), pya.Point(184, 256), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_30)

polygon_N8_31 = pya.Polygon([ pya.Point(1048, 80), pya.Point(1120, 80), pya.Point(1120, 832), pya.Point(1048, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_31)

polygon_N9_32 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 688), pya.Point(40, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_32)

polygon_N9_33 = pya.Polygon([ pya.Point(1192, -64), pya.Point(1264, -64), pya.Point(1264, 688), pya.Point(1192, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_33)

polygon_N8_34 = pya.Polygon([ pya.Point(128, 140), pya.Point(1248, 140), pya.Point(1248, 212), pya.Point(128, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(20, 0))).insert(polygon_N8_34)

polygon_N1_35 = pya.Polygon([ pya.Point(328, 1148), pya.Point(400, 1148), pya.Point(400, 1220), pya.Point(328, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_35)

polygon_N1_36 = pya.Polygon([ pya.Point(328, 284), pya.Point(400, 284), pya.Point(400, 356), pya.Point(328, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_36)

polygon_N1_37 = pya.Polygon([ pya.Point(328, 140), pya.Point(400, 140), pya.Point(400, 212), pya.Point(328, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_37)

polygon_N2_38 = pya.Polygon([ pya.Point(40, 1004), pya.Point(112, 1004), pya.Point(112, 1076), pya.Point(40, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_38)

polygon_N3_39 = pya.Polygon([ pya.Point(616, 1004), pya.Point(688, 1004), pya.Point(688, 1076), pya.Point(616, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_39)

polygon_N3_40 = pya.Polygon([ pya.Point(472, 860), pya.Point(544, 860), pya.Point(544, 932), pya.Point(472, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_40)

polygon_N3_41 = pya.Polygon([ pya.Point(472, -4), pya.Point(544, -4), pya.Point(544, 68), pya.Point(472, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_41)

polygon_N3_42 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_42)

polygon_N4_43 = pya.Polygon([ pya.Point(1192, 1004), pya.Point(1264, 1004), pya.Point(1264, 1076), pya.Point(1192, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_43)

polygon_N5_44 = pya.Polygon([ pya.Point(904, 860), pya.Point(976, 860), pya.Point(976, 932), pya.Point(904, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_44)

polygon_N5_45 = pya.Polygon([ pya.Point(904, 284), pya.Point(976, 284), pya.Point(976, 356), pya.Point(904, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_45)

polygon_N5_46 = pya.Polygon([ pya.Point(904, 140), pya.Point(976, 140), pya.Point(976, 212), pya.Point(904, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_46)

polygon_N6_47 = pya.Polygon([ pya.Point(184, 716), pya.Point(256, 716), pya.Point(256, 788), pya.Point(184, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_47)

polygon_N7_48 = pya.Polygon([ pya.Point(760, 716), pya.Point(832, 716), pya.Point(832, 788), pya.Point(760, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_48)

polygon_N7_49 = pya.Polygon([ pya.Point(760, -4), pya.Point(832, -4), pya.Point(832, 68), pya.Point(760, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_49)

polygon_N8_50 = pya.Polygon([ pya.Point(1048, 716), pya.Point(1120, 716), pya.Point(1120, 788), pya.Point(1048, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_50)

polygon_N8_51 = pya.Polygon([ pya.Point(184, 140), pya.Point(256, 140), pya.Point(256, 212), pya.Point(184, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_51)

polygon_N8_52 = pya.Polygon([ pya.Point(1048, 140), pya.Point(1120, 140), pya.Point(1120, 212), pya.Point(1048, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_52)

polygon_N9_53 = pya.Polygon([ pya.Point(40, 572), pya.Point(112, 572), pya.Point(112, 644), pya.Point(40, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_53)

polygon_N9_54 = pya.Polygon([ pya.Point(1192, 572), pya.Point(1264, 572), pya.Point(1264, 644), pya.Point(1192, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_54)

polygon_N9_55 = pya.Polygon([ pya.Point(40, -4), pya.Point(112, -4), pya.Point(112, 68), pya.Point(40, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_55)

polygon_N9_56 = pya.Polygon([ pya.Point(1192, -4), pya.Point(1264, -4), pya.Point(1264, 68), pya.Point(1192, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_56)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1272, -64), pya.Point(1272, 1264), pya.Point(16, 1264)]))

layout.write("../gds/Cell30.gds")
