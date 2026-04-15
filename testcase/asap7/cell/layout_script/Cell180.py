import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell180")

polygon_N1_0 = pya.Polygon([ pya.Point(880, 1148), pya.Point(1488, 1148), pya.Point(1488, 1220), pya.Point(880, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N10_1 = pya.Polygon([ pya.Point(664, 284), pya.Point(984, 284), pya.Point(984, 356), pya.Point(664, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_1)

polygon_N11_2 = pya.Polygon([ pya.Point(16, 140), pya.Point(840, 140), pya.Point(840, 212), pya.Point(16, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_2)

polygon_N12_3 = pya.Polygon([ pya.Point(880, 140), pya.Point(1488, 140), pya.Point(1488, 212), pya.Point(880, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_3)

polygon_N13_4 = pya.Polygon([ pya.Point(232, -4), pya.Point(480, -4), pya.Point(480, 68), pya.Point(232, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_4)

polygon_N2_5 = pya.Polygon([ pya.Point(16, 1004), pya.Point(912, 1004), pya.Point(912, 1076), pya.Point(16, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_5)

polygon_N2_6 = pya.Polygon([ pya.Point(736, -4), pya.Point(912, -4), pya.Point(912, 68), pya.Point(736, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_6)

polygon_N2_7 = pya.Polygon([ pya.Point(736, 428), pya.Point(1056, 428), pya.Point(1056, 500), pya.Point(736, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_7)

polygon_N3_8 = pya.Polygon([ pya.Point(304, 572), pya.Point(1128, 572), pya.Point(1128, 644), pya.Point(304, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_8)

polygon_N3_9 = pya.Polygon([ pya.Point(232, 716), pya.Point(408, 716), pya.Point(408, 788), pya.Point(232, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_9)

polygon_N3_10 = pya.Polygon([ pya.Point(952, -4), pya.Point(1128, -4), pya.Point(1128, 68), pya.Point(952, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_10)

polygon_N3_11 = pya.Polygon([ pya.Point(952, 1004), pya.Point(1128, 1004), pya.Point(1128, 1076), pya.Point(952, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_11)

polygon_N4_12 = pya.Polygon([ pya.Point(16, -4), pya.Point(192, -4), pya.Point(192, 68), pya.Point(16, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_12)

polygon_N4_13 = pya.Polygon([ pya.Point(16, 284), pya.Point(624, 284), pya.Point(624, 356), pya.Point(16, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_13)

polygon_N4_14 = pya.Polygon([ pya.Point(448, 860), pya.Point(624, 860), pya.Point(624, 932), pya.Point(448, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_14)

polygon_N5_15 = pya.Polygon([ pya.Point(664, 860), pya.Point(1272, 860), pya.Point(1272, 932), pya.Point(664, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_15)

polygon_N6_16 = pya.Polygon([ pya.Point(16, 716), pya.Point(192, 716), pya.Point(192, 788), pya.Point(16, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_16)

polygon_N7_17 = pya.Polygon([ pya.Point(520, -4), pya.Point(696, -4), pya.Point(696, 68), pya.Point(520, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_17)

polygon_N7_18 = pya.Polygon([ pya.Point(88, 428), pya.Point(696, 428), pya.Point(696, 500), pya.Point(88, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_18)

polygon_N7_19 = pya.Polygon([ pya.Point(448, 716), pya.Point(696, 716), pya.Point(696, 788), pya.Point(448, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_19)

polygon_N8_20 = pya.Polygon([ pya.Point(1168, -4), pya.Point(1560, -4), pya.Point(1560, 68), pya.Point(1168, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_20)

polygon_N8_21 = pya.Polygon([ pya.Point(1096, 284), pya.Point(1560, 284), pya.Point(1560, 356), pya.Point(1096, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_21)

polygon_N8_22 = pya.Polygon([ pya.Point(1024, 716), pya.Point(1272, 716), pya.Point(1272, 788), pya.Point(1024, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_22)

polygon_N9_23 = pya.Polygon([ pya.Point(1384, 716), pya.Point(1560, 716), pya.Point(1560, 788), pya.Point(1384, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_23)

polygon_N10_24 = pya.Polygon([ pya.Point(904, 224), pya.Point(976, 224), pya.Point(976, 400), pya.Point(904, 400), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N10_24)

polygon_N13_25 = pya.Polygon([ pya.Point(328, -64), pya.Point(400, -64), pya.Point(400, 112), pya.Point(328, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N13_25)

polygon_N2_26 = pya.Polygon([ pya.Point(760, -64), pya.Point(832, -64), pya.Point(832, 1120), pya.Point(760, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_26)

polygon_N3_27 = pya.Polygon([ pya.Point(1048, -64), pya.Point(1120, -64), pya.Point(1120, 1120), pya.Point(1048, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_27)

polygon_N3_28 = pya.Polygon([ pya.Point(328, 512), pya.Point(400, 512), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_28)

polygon_N4_29 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 400), pya.Point(40, 400), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_29)

polygon_N4_30 = pya.Polygon([ pya.Point(472, 224), pya.Point(544, 224), pya.Point(544, 976), pya.Point(472, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_30)

polygon_N6_31 = pya.Polygon([ pya.Point(40, 656), pya.Point(112, 656), pya.Point(112, 832), pya.Point(40, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_31)

polygon_N7_32 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 832), pya.Point(616, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_32)

polygon_N8_33 = pya.Polygon([ pya.Point(1192, -64), pya.Point(1264, -64), pya.Point(1264, 832), pya.Point(1192, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_33)

polygon_N9_34 = pya.Polygon([ pya.Point(1480, 656), pya.Point(1552, 656), pya.Point(1552, 832), pya.Point(1480, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_34)

polygon_N2_35 = pya.Polygon([ pya.Point(760, 1004), pya.Point(832, 1004), pya.Point(832, 1076), pya.Point(760, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_35)

polygon_N2_36 = pya.Polygon([ pya.Point(760, 428), pya.Point(832, 428), pya.Point(832, 500), pya.Point(760, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_36)

polygon_N2_37 = pya.Polygon([ pya.Point(760, -4), pya.Point(832, -4), pya.Point(832, 68), pya.Point(760, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_37)

polygon_N3_38 = pya.Polygon([ pya.Point(1048, 1004), pya.Point(1120, 1004), pya.Point(1120, 1076), pya.Point(1048, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_38)

polygon_N3_39 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_39)

polygon_N3_40 = pya.Polygon([ pya.Point(328, 572), pya.Point(400, 572), pya.Point(400, 644), pya.Point(328, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_40)

polygon_N3_41 = pya.Polygon([ pya.Point(1048, 572), pya.Point(1120, 572), pya.Point(1120, 644), pya.Point(1048, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_41)

polygon_N3_42 = pya.Polygon([ pya.Point(1048, -4), pya.Point(1120, -4), pya.Point(1120, 68), pya.Point(1048, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_42)

polygon_N4_43 = pya.Polygon([ pya.Point(472, 860), pya.Point(544, 860), pya.Point(544, 932), pya.Point(472, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_43)

polygon_N4_44 = pya.Polygon([ pya.Point(40, 284), pya.Point(112, 284), pya.Point(112, 356), pya.Point(40, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_44)

polygon_N4_45 = pya.Polygon([ pya.Point(472, 284), pya.Point(544, 284), pya.Point(544, 356), pya.Point(472, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_45)

polygon_N4_46 = pya.Polygon([ pya.Point(40, -4), pya.Point(112, -4), pya.Point(112, 68), pya.Point(40, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_46)

polygon_N6_47 = pya.Polygon([ pya.Point(40, 716), pya.Point(112, 716), pya.Point(112, 788), pya.Point(40, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_47)

polygon_N7_48 = pya.Polygon([ pya.Point(616, 716), pya.Point(688, 716), pya.Point(688, 788), pya.Point(616, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_48)

polygon_N7_49 = pya.Polygon([ pya.Point(616, 428), pya.Point(688, 428), pya.Point(688, 500), pya.Point(616, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_49)

polygon_N7_50 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_50)

polygon_N8_51 = pya.Polygon([ pya.Point(1192, 716), pya.Point(1264, 716), pya.Point(1264, 788), pya.Point(1192, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_51)

polygon_N8_52 = pya.Polygon([ pya.Point(1192, 284), pya.Point(1264, 284), pya.Point(1264, 356), pya.Point(1192, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_52)

polygon_N8_53 = pya.Polygon([ pya.Point(1192, -4), pya.Point(1264, -4), pya.Point(1264, 68), pya.Point(1192, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_53)

polygon_N9_54 = pya.Polygon([ pya.Point(1480, 716), pya.Point(1552, 716), pya.Point(1552, 788), pya.Point(1480, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_54)

polygon_N10_55 = pya.Polygon([ pya.Point(904, 284), pya.Point(976, 284), pya.Point(976, 356), pya.Point(904, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N10_55)

polygon_N13_56 = pya.Polygon([ pya.Point(328, -4), pya.Point(400, -4), pya.Point(400, 68), pya.Point(328, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_56)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1560, -64), pya.Point(1560, 1220), pya.Point(16, 1220)]))

layout.write("../gds/Cell180.gds")
