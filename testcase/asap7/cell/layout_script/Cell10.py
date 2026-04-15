import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell10")

polygon_N1_0 = pya.Polygon([ pya.Point(592, 1148), pya.Point(2280, 1148), pya.Point(2280, 1220), pya.Point(592, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N10_1 = pya.Polygon([ pya.Point(16, 140), pya.Point(408, 140), pya.Point(408, 212), pya.Point(16, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_1)

polygon_N11_2 = pya.Polygon([ pya.Point(16, -4), pya.Point(192, -4), pya.Point(192, 68), pya.Point(16, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_2)

polygon_N2_3 = pya.Polygon([ pya.Point(16, 572), pya.Point(696, 572), pya.Point(696, 644), pya.Point(16, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_3)

polygon_N2_4 = pya.Polygon([ pya.Point(16, 716), pya.Point(192, 716), pya.Point(192, 788), pya.Point(16, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_4)

polygon_N2_5 = pya.Polygon([ pya.Point(16, 1004), pya.Point(336, 1004), pya.Point(336, 1076), pya.Point(16, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_5)

polygon_N2_6 = pya.Polygon([ pya.Point(376, -4), pya.Point(696, -4), pya.Point(696, 68), pya.Point(376, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_6)

polygon_N2_7 = pya.Polygon([ pya.Point(520, 428), pya.Point(696, 428), pya.Point(696, 500), pya.Point(520, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_7)

polygon_N3_8 = pya.Polygon([ pya.Point(1096, 284), pya.Point(2712, 284), pya.Point(2712, 356), pya.Point(1096, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_8)

polygon_N3_9 = pya.Polygon([ pya.Point(736, 716), pya.Point(2712, 716), pya.Point(2712, 788), pya.Point(736, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_9)

polygon_N3_10 = pya.Polygon([ pya.Point(448, 1004), pya.Point(840, 1004), pya.Point(840, 1076), pya.Point(448, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_10)

polygon_N4_11 = pya.Polygon([ pya.Point(664, 140), pya.Point(1704, 140), pya.Point(1704, 212), pya.Point(664, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_11)

polygon_N4_12 = pya.Polygon([ pya.Point(1384, 860), pya.Point(1704, 860), pya.Point(1704, 932), pya.Point(1384, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_12)

polygon_N4_13 = pya.Polygon([ pya.Point(1600, 1004), pya.Point(2352, 1004), pya.Point(2352, 1076), pya.Point(1600, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_13)

polygon_N5_14 = pya.Polygon([ pya.Point(1312, -4), pya.Point(2568, -4), pya.Point(2568, 68), pya.Point(1312, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_14)

polygon_N5_15 = pya.Polygon([ pya.Point(1024, 428), pya.Point(1416, 428), pya.Point(1416, 500), pya.Point(1024, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_15)

polygon_N5_16 = pya.Polygon([ pya.Point(2320, 860), pya.Point(2712, 860), pya.Point(2712, 932), pya.Point(2320, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_16)

polygon_N5_17 = pya.Polygon([ pya.Point(2464, 1004), pya.Point(2640, 1004), pya.Point(2640, 1076), pya.Point(2464, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_17)

polygon_N6_18 = pya.Polygon([ pya.Point(88, 860), pya.Point(1344, 860), pya.Point(1344, 932), pya.Point(88, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_18)

polygon_N7_19 = pya.Polygon([ pya.Point(448, 140), pya.Point(624, 140), pya.Point(624, 212), pya.Point(448, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_19)

polygon_N7_20 = pya.Polygon([ pya.Point(304, 428), pya.Point(480, 428), pya.Point(480, 500), pya.Point(304, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_20)

polygon_N7_21 = pya.Polygon([ pya.Point(304, 716), pya.Point(552, 716), pya.Point(552, 788), pya.Point(304, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_21)

polygon_N8_22 = pya.Polygon([ pya.Point(160, 284), pya.Point(336, 284), pya.Point(336, 356), pya.Point(160, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_22)

polygon_N9_23 = pya.Polygon([ pya.Point(448, 284), pya.Point(912, 284), pya.Point(912, 356), pya.Point(448, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_23)

polygon_N11_24 = pya.Polygon([ pya.Point(40, -64), pya.Point(112, -64), pya.Point(112, 112), pya.Point(40, 112), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N11_24)

polygon_N2_25 = pya.Polygon([ pya.Point(616, -64), pya.Point(688, -64), pya.Point(688, 688), pya.Point(616, 688), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_25)

polygon_N2_26 = pya.Polygon([ pya.Point(40, 512), pya.Point(112, 512), pya.Point(112, 832), pya.Point(40, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_26)

polygon_N3_27 = pya.Polygon([ pya.Point(2632, 224), pya.Point(2704, 224), pya.Point(2704, 832), pya.Point(2632, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_27)

polygon_N4_28 = pya.Polygon([ pya.Point(1624, 80), pya.Point(1696, 80), pya.Point(1696, 1120), pya.Point(1624, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_28)

polygon_N5_29 = pya.Polygon([ pya.Point(2488, -64), pya.Point(2560, -64), pya.Point(2560, 1120), pya.Point(2488, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_29)

polygon_N6_30 = pya.Polygon([ pya.Point(1048, 800), pya.Point(1120, 800), pya.Point(1120, 976), pya.Point(1048, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_30)

polygon_N7_31 = pya.Polygon([ pya.Point(472, 80), pya.Point(544, 80), pya.Point(544, 832), pya.Point(472, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_31)

polygon_N7_32 = pya.Polygon([ pya.Point(328, 368), pya.Point(400, 368), pya.Point(400, 832), pya.Point(328, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_32)

polygon_N8_33 = pya.Polygon([ pya.Point(184, 224), pya.Point(256, 224), pya.Point(256, 400), pya.Point(184, 400), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_33)

polygon_N2_34 = pya.Polygon([ pya.Point(40, 716), pya.Point(112, 716), pya.Point(112, 788), pya.Point(40, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_34)

polygon_N2_35 = pya.Polygon([ pya.Point(40, 572), pya.Point(112, 572), pya.Point(112, 644), pya.Point(40, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_35)

polygon_N2_36 = pya.Polygon([ pya.Point(616, 572), pya.Point(688, 572), pya.Point(688, 644), pya.Point(616, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_36)

polygon_N2_37 = pya.Polygon([ pya.Point(616, 428), pya.Point(688, 428), pya.Point(688, 500), pya.Point(616, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_37)

polygon_N2_38 = pya.Polygon([ pya.Point(616, -4), pya.Point(688, -4), pya.Point(688, 68), pya.Point(616, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_38)

polygon_N3_39 = pya.Polygon([ pya.Point(2632, 716), pya.Point(2704, 716), pya.Point(2704, 788), pya.Point(2632, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_39)

polygon_N3_40 = pya.Polygon([ pya.Point(2632, 284), pya.Point(2704, 284), pya.Point(2704, 356), pya.Point(2632, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_40)

polygon_N4_41 = pya.Polygon([ pya.Point(1624, 1004), pya.Point(1696, 1004), pya.Point(1696, 1076), pya.Point(1624, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_41)

polygon_N4_42 = pya.Polygon([ pya.Point(1624, 860), pya.Point(1696, 860), pya.Point(1696, 932), pya.Point(1624, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_42)

polygon_N4_43 = pya.Polygon([ pya.Point(1624, 140), pya.Point(1696, 140), pya.Point(1696, 212), pya.Point(1624, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_43)

polygon_N5_44 = pya.Polygon([ pya.Point(2488, 1004), pya.Point(2560, 1004), pya.Point(2560, 1076), pya.Point(2488, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_44)

polygon_N5_45 = pya.Polygon([ pya.Point(2488, 860), pya.Point(2560, 860), pya.Point(2560, 932), pya.Point(2488, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_45)

polygon_N5_46 = pya.Polygon([ pya.Point(2488, -4), pya.Point(2560, -4), pya.Point(2560, 68), pya.Point(2488, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_46)

polygon_N6_47 = pya.Polygon([ pya.Point(1048, 860), pya.Point(1120, 860), pya.Point(1120, 932), pya.Point(1048, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_47)

polygon_N7_48 = pya.Polygon([ pya.Point(328, 716), pya.Point(400, 716), pya.Point(400, 788), pya.Point(328, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_48)

polygon_N7_49 = pya.Polygon([ pya.Point(472, 716), pya.Point(544, 716), pya.Point(544, 788), pya.Point(472, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_49)

polygon_N7_50 = pya.Polygon([ pya.Point(328, 428), pya.Point(400, 428), pya.Point(400, 500), pya.Point(328, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_50)

polygon_N7_51 = pya.Polygon([ pya.Point(472, 140), pya.Point(544, 140), pya.Point(544, 212), pya.Point(472, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_51)

polygon_N8_52 = pya.Polygon([ pya.Point(184, 284), pya.Point(256, 284), pya.Point(256, 356), pya.Point(184, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_52)

polygon_N11_53 = pya.Polygon([ pya.Point(40, -4), pya.Point(112, -4), pya.Point(112, 68), pya.Point(40, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N11_53)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(2712, -64), pya.Point(2712, 1220), pya.Point(16, 1220)]))

layout.write("../gds/Cell10.gds")
