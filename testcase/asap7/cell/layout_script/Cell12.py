import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("Cell12")

polygon_N1_0 = pya.Polygon([ pya.Point(2680, 428), pya.Point(2856, 428), pya.Point(2856, 500), pya.Point(2680, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_0)

polygon_N1_1 = pya.Polygon([ pya.Point(2680, 716), pya.Point(2856, 716), pya.Point(2856, 788), pya.Point(2680, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_1)

polygon_N1_2 = pya.Polygon([ pya.Point(2752, 1148), pya.Point(3072, 1148), pya.Point(3072, 1220), pya.Point(2752, 1220), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N1_2)

polygon_N10_3 = pya.Polygon([ pya.Point(2896, 428), pya.Point(3288, 428), pya.Point(3288, 500), pya.Point(2896, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N10_3)

polygon_N11_4 = pya.Polygon([ pya.Point(2752, 284), pya.Point(3144, 284), pya.Point(3144, 356), pya.Point(2752, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N11_4)

polygon_N12_5 = pya.Polygon([ pya.Point(3256, 284), pya.Point(3432, 284), pya.Point(3432, 356), pya.Point(3256, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N12_5)

polygon_N13_6 = pya.Polygon([ pya.Point(2896, 140), pya.Point(3072, 140), pya.Point(3072, 212), pya.Point(2896, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N13_6)

polygon_N14_7 = pya.Polygon([ pya.Point(2752, -4), pya.Point(3432, -4), pya.Point(3432, 68), pya.Point(2752, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N14_7)

polygon_N2_8 = pya.Polygon([ pya.Point(88, 140), pya.Point(2136, 140), pya.Point(2136, 212), pya.Point(88, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_8)

polygon_N2_9 = pya.Polygon([ pya.Point(88, 860), pya.Point(2136, 860), pya.Point(2136, 932), pya.Point(88, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_9)

polygon_N2_10 = pya.Polygon([ pya.Point(1312, 284), pya.Point(1992, 284), pya.Point(1992, 356), pya.Point(1312, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_10)

polygon_N2_11 = pya.Polygon([ pya.Point(1888, 1004), pya.Point(2064, 1004), pya.Point(2064, 1076), pya.Point(1888, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N2_11)

polygon_N3_12 = pya.Polygon([ pya.Point(1240, -4), pya.Point(2352, -4), pya.Point(2352, 68), pya.Point(1240, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_12)

polygon_N3_13 = pya.Polygon([ pya.Point(1600, 716), pya.Point(1776, 716), pya.Point(1776, 788), pya.Point(1600, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_13)

polygon_N3_14 = pya.Polygon([ pya.Point(2104, 1004), pya.Point(3216, 1004), pya.Point(3216, 1076), pya.Point(2104, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N3_14)

polygon_N4_15 = pya.Polygon([ pya.Point(2608, 140), pya.Point(2784, 140), pya.Point(2784, 212), pya.Point(2608, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_15)

polygon_N4_16 = pya.Polygon([ pya.Point(2320, 860), pya.Point(3072, 860), pya.Point(3072, 932), pya.Point(2320, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N4_16)

polygon_N5_17 = pya.Polygon([ pya.Point(3256, 860), pya.Point(3432, 860), pya.Point(3432, 932), pya.Point(3256, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N5_17)

polygon_N6_18 = pya.Polygon([ pya.Point(160, -4), pya.Point(1128, -4), pya.Point(1128, 68), pya.Point(160, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_18)

polygon_N6_19 = pya.Polygon([ pya.Point(16, 716), pya.Point(1560, 716), pya.Point(1560, 788), pya.Point(16, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N6_19)

polygon_N7_20 = pya.Polygon([ pya.Point(1384, 428), pya.Point(2208, 428), pya.Point(2208, 500), pya.Point(1384, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_20)

polygon_N7_21 = pya.Polygon([ pya.Point(1816, 716), pya.Point(2352, 716), pya.Point(2352, 788), pya.Point(1816, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N7_21)

polygon_N8_22 = pya.Polygon([ pya.Point(2464, -4), pya.Point(2712, -4), pya.Point(2712, 68), pya.Point(2464, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_22)

polygon_N8_23 = pya.Polygon([ pya.Point(2464, 572), pya.Point(3000, 572), pya.Point(3000, 644), pya.Point(2464, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_23)

polygon_N8_24 = pya.Polygon([ pya.Point(2464, 716), pya.Point(2640, 716), pya.Point(2640, 788), pya.Point(2464, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_24)

polygon_N8_25 = pya.Polygon([ pya.Point(2896, 716), pya.Point(3072, 716), pya.Point(3072, 788), pya.Point(2896, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N8_25)

polygon_N9_26 = pya.Polygon([ pya.Point(3112, 140), pya.Point(3288, 140), pya.Point(3288, 212), pya.Point(3112, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_26)

polygon_N9_27 = pya.Polygon([ pya.Point(3184, 716), pya.Point(3432, 716), pya.Point(3432, 788), pya.Point(3184, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(0, 0))).insert(polygon_N9_27)

polygon_N1_28 = pya.Polygon([ pya.Point(2776, 368), pya.Point(2848, 368), pya.Point(2848, 832), pya.Point(2776, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N1_28)

polygon_N12_29 = pya.Polygon([ pya.Point(3352, 224), pya.Point(3424, 224), pya.Point(3424, 400), pya.Point(3352, 400), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N12_29)

polygon_N13_30 = pya.Polygon([ pya.Point(2920, 80), pya.Point(2992, 80), pya.Point(2992, 256), pya.Point(2920, 256), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N13_30)

polygon_N2_31 = pya.Polygon([ pya.Point(1912, 80), pya.Point(1984, 80), pya.Point(1984, 1120), pya.Point(1912, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N2_31)

polygon_N3_32 = pya.Polygon([ pya.Point(1624, -64), pya.Point(1696, -64), pya.Point(1696, 832), pya.Point(1624, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_32)

polygon_N3_33 = pya.Polygon([ pya.Point(2200, -64), pya.Point(2272, -64), pya.Point(2272, 1120), pya.Point(2200, 1120), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N3_33)

polygon_N4_34 = pya.Polygon([ pya.Point(2632, 80), pya.Point(2704, 80), pya.Point(2704, 976), pya.Point(2632, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N4_34)

polygon_N5_35 = pya.Polygon([ pya.Point(3352, 800), pya.Point(3424, 800), pya.Point(3424, 976), pya.Point(3352, 976), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N5_35)

polygon_N6_36 = pya.Polygon([ pya.Point(1048, -64), pya.Point(1120, -64), pya.Point(1120, 832), pya.Point(1048, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N6_36)

polygon_N7_37 = pya.Polygon([ pya.Point(2056, 368), pya.Point(2128, 368), pya.Point(2128, 832), pya.Point(2056, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N7_37)

polygon_N8_38 = pya.Polygon([ pya.Point(2488, -64), pya.Point(2560, -64), pya.Point(2560, 832), pya.Point(2488, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_38)

polygon_N8_39 = pya.Polygon([ pya.Point(2920, 512), pya.Point(2992, 512), pya.Point(2992, 832), pya.Point(2920, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N8_39)

polygon_N9_40 = pya.Polygon([ pya.Point(3208, 80), pya.Point(3280, 80), pya.Point(3280, 832), pya.Point(3208, 832), ])
top_cell.shapes(layout.layer(pya.LayerInfo(19, 0))).insert(polygon_N9_40)

polygon_N1_41 = pya.Polygon([ pya.Point(2776, 716), pya.Point(2848, 716), pya.Point(2848, 788), pya.Point(2776, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_41)

polygon_N1_42 = pya.Polygon([ pya.Point(2776, 428), pya.Point(2848, 428), pya.Point(2848, 500), pya.Point(2776, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N1_42)

polygon_N2_43 = pya.Polygon([ pya.Point(1912, 1004), pya.Point(1984, 1004), pya.Point(1984, 1076), pya.Point(1912, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_43)

polygon_N2_44 = pya.Polygon([ pya.Point(1912, 860), pya.Point(1984, 860), pya.Point(1984, 932), pya.Point(1912, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_44)

polygon_N2_45 = pya.Polygon([ pya.Point(1912, 284), pya.Point(1984, 284), pya.Point(1984, 356), pya.Point(1912, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_45)

polygon_N2_46 = pya.Polygon([ pya.Point(1912, 140), pya.Point(1984, 140), pya.Point(1984, 212), pya.Point(1912, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N2_46)

polygon_N3_47 = pya.Polygon([ pya.Point(2200, 1004), pya.Point(2272, 1004), pya.Point(2272, 1076), pya.Point(2200, 1076), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_47)

polygon_N3_48 = pya.Polygon([ pya.Point(1624, 716), pya.Point(1696, 716), pya.Point(1696, 788), pya.Point(1624, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_48)

polygon_N3_49 = pya.Polygon([ pya.Point(1624, -4), pya.Point(1696, -4), pya.Point(1696, 68), pya.Point(1624, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_49)

polygon_N3_50 = pya.Polygon([ pya.Point(2200, -4), pya.Point(2272, -4), pya.Point(2272, 68), pya.Point(2200, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N3_50)

polygon_N4_51 = pya.Polygon([ pya.Point(2632, 860), pya.Point(2704, 860), pya.Point(2704, 932), pya.Point(2632, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_51)

polygon_N4_52 = pya.Polygon([ pya.Point(2632, 140), pya.Point(2704, 140), pya.Point(2704, 212), pya.Point(2632, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N4_52)

polygon_N5_53 = pya.Polygon([ pya.Point(3352, 860), pya.Point(3424, 860), pya.Point(3424, 932), pya.Point(3352, 932), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N5_53)

polygon_N6_54 = pya.Polygon([ pya.Point(1048, 716), pya.Point(1120, 716), pya.Point(1120, 788), pya.Point(1048, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_54)

polygon_N6_55 = pya.Polygon([ pya.Point(1048, -4), pya.Point(1120, -4), pya.Point(1120, 68), pya.Point(1048, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N6_55)

polygon_N7_56 = pya.Polygon([ pya.Point(2056, 716), pya.Point(2128, 716), pya.Point(2128, 788), pya.Point(2056, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_56)

polygon_N7_57 = pya.Polygon([ pya.Point(2056, 428), pya.Point(2128, 428), pya.Point(2128, 500), pya.Point(2056, 500), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N7_57)

polygon_N8_58 = pya.Polygon([ pya.Point(2488, 716), pya.Point(2560, 716), pya.Point(2560, 788), pya.Point(2488, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_58)

polygon_N8_59 = pya.Polygon([ pya.Point(2920, 716), pya.Point(2992, 716), pya.Point(2992, 788), pya.Point(2920, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_59)

polygon_N8_60 = pya.Polygon([ pya.Point(2488, 572), pya.Point(2560, 572), pya.Point(2560, 644), pya.Point(2488, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_60)

polygon_N8_61 = pya.Polygon([ pya.Point(2920, 572), pya.Point(2992, 572), pya.Point(2992, 644), pya.Point(2920, 644), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_61)

polygon_N8_62 = pya.Polygon([ pya.Point(2488, -4), pya.Point(2560, -4), pya.Point(2560, 68), pya.Point(2488, 68), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N8_62)

polygon_N9_63 = pya.Polygon([ pya.Point(3208, 716), pya.Point(3280, 716), pya.Point(3280, 788), pya.Point(3208, 788), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_63)

polygon_N9_64 = pya.Polygon([ pya.Point(3208, 140), pya.Point(3280, 140), pya.Point(3280, 212), pya.Point(3208, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N9_64)

polygon_N12_65 = pya.Polygon([ pya.Point(3352, 284), pya.Point(3424, 284), pya.Point(3424, 356), pya.Point(3352, 356), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N12_65)

polygon_N13_66 = pya.Polygon([ pya.Point(2920, 140), pya.Point(2992, 140), pya.Point(2992, 212), pya.Point(2920, 212), ])
top_cell.shapes(layout.layer(pya.LayerInfo(18, 0))).insert(polygon_N13_66)


cell_box = layout.layer(pya.LayerInfo(235, 0))
top_cell.shapes(cell_box).insert(pya.Polygon([pya.Point(16, -64), pya.Point(3432, -64), pya.Point(3432, 1220), pya.Point(16, 1220)]))

layout.write("../gds/Cell12.gds")
