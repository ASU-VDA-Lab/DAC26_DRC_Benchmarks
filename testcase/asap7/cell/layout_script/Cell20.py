import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell20")

polygon_N1_0 = pya.Polygon([ pya.Point(592, 716), pya.Point(768, 716), pya.Point(768, 788), pya.Point(592, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(664, 1148), pya.Point(1200, 1148), pya.Point(1200, 1220), pya.Point(664, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N2_2 = pya.Polygon([ pya.Point(16, 1004), pya.Point(1056, 1004), pya.Point(1056, 1076), pya.Point(16, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_2)

polygon_N2_3 = pya.Polygon([ pya.Point(736, 428), pya.Point(1056, 428), pya.Point(1056, 500), pya.Point(736, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_3)

polygon_N3_4 = pya.Polygon([ pya.Point(88, 284), pya.Point(624, 284), pya.Point(624, 356), pya.Point(88, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_4)

polygon_N3_5 = pya.Polygon([ pya.Point(232, 860), pya.Point(984, 860), pya.Point(984, 932), pya.Point(232, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_5)

polygon_N3_6 = pya.Polygon([ pya.Point(520, -4), pya.Point(984, -4), pya.Point(984, 68), pya.Point(520, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_6)

polygon_N4_7 = pya.Polygon([ pya.Point(160, 140), pya.Point(1128, 140), pya.Point(1128, 212), pya.Point(160, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_7)

polygon_N4_8 = pya.Polygon([ pya.Point(88, 716), pya.Point(264, 716), pya.Point(264, 788), pya.Point(88, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_8)

polygon_N4_9 = pya.Polygon([ pya.Point(808, 716), pya.Point(1128, 716), pya.Point(1128, 788), pya.Point(808, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_9)

polygon_N5_10 = pya.Polygon([ pya.Point(160, -4), pya.Point(408, -4), pya.Point(408, 68), pya.Point(160, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_10)

polygon_N5_11 = pya.Polygon([ pya.Point(160, 428), pya.Point(552, 428), pya.Point(552, 500), pya.Point(160, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_11)

polygon_N5_12 = pya.Polygon([ pya.Point(304, 716), pya.Point(480, 716), pya.Point(480, 788), pya.Point(304, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_12)

polygon_N6_13 = pya.Polygon([ pya.Point(1096, -4), pya.Point(1272, -4), pya.Point(1272, 68), pya.Point(1096, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_13)

polygon_N6_14 = pya.Polygon([ pya.Point(664, 284), pya.Point(1200, 284), pya.Point(1200, 356), pya.Point(664, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_14)

polygon_N1_15 = pya.Polygon([ pya.Point(616, 656), pya.Point(688, 656), pya.Point(688, 832), pya.Point(616, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_15)

polygon_N2_16 = pya.Polygon([ pya.Point(760, 368), pya.Point(832, 368), pya.Point(832, 1120), pya.Point(760, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_16)

polygon_N3_17 = pya.Polygon([ pya.Point(904, -64), pya.Point(976, -64), pya.Point(976, 976), pya.Point(904, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_17)

polygon_N4_18 = pya.Polygon([ pya.Point(184, 80), pya.Point(256, 80), pya.Point(256, 832), pya.Point(184, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_18)

polygon_N4_19 = pya.Polygon([ pya.Point(1048, 80), pya.Point(1120, 80), pya.Point(1120, 832), pya.Point(1048, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_19)

polygon_N5_20 = pya.Polygon([ pya.Point(328, -64), pya.Point(400, -64), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_20)

polygon_N6_21 = pya.Polygon([ pya.Point(1192, -64), pya.Point(1264, -64), pya.Point(1264, 112), pya.Point(1192, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_21)

polygon_N7_22 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 112), pya.Point(40, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_22)

polygon_N1_23 = pya.Polygon([ pya.Point(616, 716), pya.Point(688, 716), pya.Point(688, 788), pya.Point(616, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_23)

polygon_N2_24 = pya.Polygon([ pya.Point(760, 1004), pya.Point(832, 1004), pya.Point(832, 1076), pya.Point(760, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_24)

polygon_N2_25 = pya.Polygon([ pya.Point(760, 428), pya.Point(832, 428), pya.Point(832, 500), pya.Point(760, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_25)

polygon_N3_26 = pya.Polygon([ pya.Point(904, 860), pya.Point(976, 860), pya.Point(976, 932), pya.Point(904, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_26)

polygon_N3_27 = pya.Polygon([ pya.Point(904, -4), pya.Point(976, -4), pya.Point(976, 68), pya.Point(904, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_27)

polygon_N4_28 = pya.Polygon([ pya.Point(184, 716), pya.Point(256, 716), pya.Point(256, 788), pya.Point(184, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_28)

polygon_N4_29 = pya.Polygon([ pya.Point(1048, 716), pya.Point(1120, 716), pya.Point(1120, 788), pya.Point(1048, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_29)

polygon_N4_30 = pya.Polygon([ pya.Point(184, 140), pya.Point(256, 140), pya.Point(256, 212), pya.Point(184, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_30)

polygon_N4_31 = pya.Polygon([ pya.Point(1048, 140), pya.Point(1120, 140), pya.Point(1120, 212), pya.Point(1048, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_31)

polygon_N5_32 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_32)

polygon_N5_33 = pya.Polygon([ pya.Point(328, 428), pya.Point(400, 428), pya.Point(400, 500), pya.Point(328, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_33)

polygon_N5_34 = pya.Polygon([ pya.Point(328, -4), pya.Point(400, -4), pya.Point(400, 68), pya.Point(328, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_34)

polygon_N6_35 = pya.Polygon([ pya.Point(1192, -4), pya.Point(1264, -4), pya.Point(1264, 68), pya.Point(1192, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_35)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(1272, -64), pya.Point(1272, 1220), pya.Point(16, 1220)]))

layout.write("../gds/Cell20.gds")
