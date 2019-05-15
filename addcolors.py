from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Category, Color

engine = create_engine('sqlite:///colors.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add Default User
user1 = User(name="default", email="none", picture="none")

# Add Categories
category1 = Category(name="Red", user=user1)
session.add(category1)
session.commit()

category2 = Category(name="Pink", user=user1)
session.add(category2)
session.commit()

category3 = Category(name="Orange", user=user1)
session.add(category3)
session.commit()

category4 = Category(name="Yellow", user=user1)
session.add(category4)
session.commit()

category5 = Category(name="Purple", user=user1)
session.add(category5)
session.commit()

category6 = Category(name="Green", user=user1)
session.add(category6)
session.commit()

category7 = Category(name="Blue", user=user1)
session.add(category7)
session.commit()

category8 = Category(name="Brown", user=user1)
session.add(category8)
session.commit()

category9 = Category(name="White", user=user1)
session.add(category9)
session.commit()

category10 = Category(name="Gray", user=user1)
session.add(category10)
session.commit()

# Add colors
# REDs (9)

color1 = Color(name="INDIANRED", hex_code="#CD5C5C",
               rgb_code="RGB(205, 92, 92)", category=category1, user=user1)
session.add(color1)
session.commit()

color2 = Color(name="LIGHTCORAL", hex_code="#F08080",
               rgb_code="RGB(240, 128, 128)", category=category1, user=user1)
session.add(color2)
session.commit()

color3 = Color(name="SALMON", hex_code="#FA8072",
               rgb_code="RGB(250, 128, 114)", category=category1, user=user1)
session.add(color3)
session.commit()

color4 = Color(name="DARKSALMON", hex_code="#E9967A",
               rgb_code="RGB(233, 150, 122)", category=category1, user=user1)
session.add(color4)
session.commit()

color5 = Color(name="LIGHTSALMON", hex_code="#FFA07A",
               rgb_code="RGB(255, 160, 122)", category=category1, user=user1)
session.add(color5)
session.commit()

color6 = Color(name="CRIMSON", hex_code="#DC143C",
               rgb_code="RGB(220, 20, 60)", category=category1, user=user1)
session.add(color6)
session.commit()

color7 = Color(name="RED", hex_code="#FF0000",
               rgb_code="RGB(255, 0, 0)", category=category1, user=user1)
session.add(color7)
session.commit()

color8 = Color(name="FIREBRICK", hex_code="#B22222",
               rgb_code="RGB(178, 34, 34)", category=category1, user=user1)
session.add(color8)
session.commit()

color9 = Color(name="DARKRED", hex_code="#8B0000",
               rgb_code="RGB(139, 0, 0)", category=category1, user=user1)
session.add(color9)
session.commit()

# PINKs (6)

color10 = Color(name="PINK", hex_code="#FFC0CB",
                rgb_code="RGB(255, 192, 203)", category=category2, user=user1)
session.add(color10)
session.commit()

color11 = Color(name="LIGHTPINK", hex_code="#FFB6C1",
                rgb_code="RGB(255, 182, 193)", category=category2, user=user1)
session.add(color11)
session.commit()

color12 = Color(name="HOTPINK", hex_code="#FF69B4",
                rgb_code="RGB(255, 105, 180)", category=category2, user=user1)
session.add(color12)
session.commit()

color13 = Color(name="DEEPPINK", hex_code="#FF1493",
                rgb_code="RGB(255, 20, 147)", category=category2, user=user1)
session.add(color13)
session.commit()

color14 = Color(name="MEDIUMVIOLETRED", hex_code="#C71585",
                rgb_code="RGB(199, 21, 133)", category=category2, user=user1)
session.add(color14)
session.commit()

color15 = Color(name="PALEVIOLETRED", hex_code="#DB7093",
                rgb_code="RGB(219, 112, 147)", category=category2, user=user1)
session.add(color15)
session.commit()

# ORANGEs (6)

color16 = Color(name="CORAL", hex_code="#FF7F50",
                rgb_code="RGB(255, 127, 80)", category=category3, user=user1)
session.add(color16)
session.commit()

color17 = Color(name="TOMATO", hex_code="#FF6347",
                rgb_code="RGB(255, 99, 71)", category=category3, user=user1)
session.add(color17)
session.commit()

color18 = Color(name="ORANGERED", hex_code="#FF4500",
                rgb_code="RGB(255, 69, 0)", category=category3, user=user1)
session.add(color18)
session.commit()

color19 = Color(name="DARKORANGE", hex_code="#FF8C00",
                rgb_code="RGB(255, 140, 0)", category=category3, user=user1)
session.add(color19)
session.commit()

color20 = Color(name="ORANGE", hex_code="#FFA500",
                rgb_code="RGB(255, 165, 0)", category=category3, user=user1)
session.add(color20)
session.commit()

# YELLOWs (11)

color21 = Color(name="GOLD", hex_code="#FFD700",
                rgb_code="RGB(255, 215, 0)", category=category4, user=user1)
session.add(color21)
session.commit()

color22 = Color(name="YELLOW", hex_code="#FFFF00",
                rgb_code="RGB(255, 255, 0)", category=category4, user=user1)
session.add(color22)
session.commit()

color23 = Color(name="LIGHTYELLOW", hex_code="#FFFFE0",
                rgb_code="RGB(255, 255, 224)", category=category4, user=user1)
session.add(color23)
session.commit()

color24 = Color(name="LEMONCHIFFON", hex_code="#FFFACD",
                rgb_code="RGB(255, 250, 205)", category=category4, user=user1)
session.add(color24)
session.commit()

color25 = Color(name="LIGHTGOLDENRODYELLOW", hex_code="#FAFAD2",
                rgb_code="RGB(250, 250, 210)", category=category4, user=user1)
session.add(color25)
session.commit()

color26 = Color(name="PAPAYAWHIP", hex_code="#FFEFD5",
                rgb_code="RGB(255, 239, 213)", category=category4, user=user1)
session.add(color26)
session.commit()

color27 = Color(name="MOCCASIN", hex_code="#FFE4B5",
                rgb_code="RGB(255, 228, 181)", category=category4, user=user1)
session.add(color27)
session.commit()

color28 = Color(name="MOCCASIN", hex_code="#FFE4B5",
                rgb_code="RGB(255, 228, 181)", category=category4, user=user1)
session.add(color28)
session.commit()

color29 = Color(name="PEACHPUFF", hex_code="#FFDAB9",
                rgb_code="RGB(255, 218, 185)", category=category4, user=user1)
session.add(color29)
session.commit()

color30 = Color(name="PALEGOLDENROD", hex_code="#EEE8AA",
                rgb_code="RGB(238, 232, 170)", category=category4, user=user1)
session.add(color30)
session.commit()

color31 = Color(name="KHAKI", hex_code="#F0E68C",
                rgb_code="RGB(240, 230, 140)", category=category4, user=user1)
session.add(color31)
session.commit()

color32 = Color(name="DARKKHAKI", hex_code="#BDB76B",
                rgb_code="RGB(189, 183, 107)", category=category4, user=user1)
session.add(color32)
session.commit()

# PURPLEs (19)

color33 = Color(name="LAVENDER", hex_code="#E6E6FA",
                rgb_code="RGB(230, 230, 250)", category=category5, user=user1)
session.add(color33)
session.commit()

color34 = Color(name="THISTLE", hex_code="#D8BFD8",
                rgb_code="RGB(216, 191, 216)", category=category5, user=user1)
session.add(color34)
session.commit()

color35 = Color(name="PLUM", hex_code="#DDA0DD",
                rgb_code="RGB(221, 160, 221)", category=category5, user=user1)
session.add(color35)
session.commit()

color36 = Color(name="VIOLET", hex_code="#EE82EE",
                rgb_code="RGB(238, 130, 238)", category=category5, user=user1)
session.add(color36)
session.commit()

color37 = Color(name="ORCHID", hex_code="#DA70D6",
                rgb_code="RGB(218, 112, 214)", category=category5, user=user1)
session.add(color37)
session.commit()

color38 = Color(name="FUCHSIA", hex_code="#FF00FF",
                rgb_code="RGB(255, 0, 255)", category=category5, user=user1)
session.add(color38)
session.commit()

color39 = Color(name="MAGENTA", hex_code="#FF00FF",
                rgb_code="RGB(255, 0, 255)", category=category5, user=user1)
session.add(color39)
session.commit()

color40 = Color(name="MEDIUMORCHID", hex_code="#BA55D3",
                rgb_code="RGB(186, 85, 211)", category=category5, user=user1)
session.add(color40)
session.commit()

color41 = Color(name="MEDIUMPURPLE", hex_code="#9370DB",
                rgb_code="RGB(147, 112, 219)", category=category5, user=user1)
session.add(color41)
session.commit()

color42 = Color(name="REBECCAPURPLE", hex_code="#663399",
                rgb_code="RGB(102, 51, 153)", category=category5, user=user1)
session.add(color42)
session.commit()

color43 = Color(name="BLUEVIOLET", hex_code="#8A2BE2",
                rgb_code="RGB(138, 43, 226)", category=category5, user=user1)
session.add(color43)
session.commit()

color44 = Color(name="DARKVIOLET", hex_code="#9400D3",
                rgb_code="RGB(148, 0, 211)", category=category5, user=user1)
session.add(color44)
session.commit()

color45 = Color(name="DARKORCHID", hex_code="#9932CC",
                rgb_code="RGB(153, 50, 204)", category=category5, user=user1)
session.add(color45)
session.commit()

color46 = Color(name="DARKMAGENTA", hex_code="#8B008B",
                rgb_code="RGB(139, 0, 139))", category=category5, user=user1)
session.add(color46)
session.commit()

color47 = Color(name="PURPLE", hex_code="#800080",
                rgb_code="RGB(128, 0, 128)", category=category5, user=user1)
session.add(color47)
session.commit()

color48 = Color(name="INDIGO", hex_code="#4B0082",
                rgb_code="RGB(75, 0, 130)", category=category5, user=user1)
session.add(color48)
session.commit()

color49 = Color(name="SLATEBLUE", hex_code="#6A5ACD",
                rgb_code="RGB(106, 90, 205)", category=category5, user=user1)
session.add(color49)
session.commit()

color50 = Color(name="DARKSLATEBLUE", hex_code="#483D8B",
                rgb_code="RGB(72, 61, 139)", category=category5, user=user1)
session.add(color50)
session.commit()

color51 = Color(name="MEDIUMSLATEBLUE", hex_code="#7B68EE",
                rgb_code="RGB(123, 104, 238)", category=category5, user=user1)
session.add(color51)
session.commit()

# GREENs (23)

color52 = Color(name="GREENYELLOW", hex_code="#ADFF2F",
                rgb_code="RGB(173, 255, 47)", category=category6, user=user1)
session.add(color52)
session.commit()

color53 = Color(name="CHARTREUSE", hex_code="#7FFF00",
                rgb_code="RGB(127, 255, 0)", category=category6, user=user1)
session.add(color53)
session.commit()

color54 = Color(name="LAWNGREEN", hex_code="#7CFC00",
                rgb_code="RGB(124, 252, 0)", category=category6, user=user1)
session.add(color54)
session.commit()

color55 = Color(name="LIME", hex_code="#00FF00",
                rgb_code="RGB(0, 255, 0)", category=category6, user=user1)
session.add(color55)
session.commit()

color56 = Color(name="LIMEGREEN", hex_code="#32CD32",
                rgb_code="RGB(50, 205, 50)", category=category6, user=user1)
session.add(color56)
session.commit()

color57 = Color(name="PALEGREEN", hex_code="#98FB98",
                rgb_code="RGB(152, 251, 152)", category=category6, user=user1)
session.add(color57)
session.commit()

color58 = Color(name="LIGHTGREEN", hex_code="#90EE90",
                rgb_code="RGB(144, 238, 144)", category=category6, user=user1)
session.add(color58)
session.commit()

color59 = Color(name="MEDIUMSPRINGGREEN", hex_code="#00FA9A",
                rgb_code="RGB(0, 250, 154)", category=category6, user=user1)
session.add(color59)
session.commit()

color60 = Color(name="SPRINGGREEN", hex_code="#00FF7F",
                rgb_code="RGB(0, 255, 127))", category=category6, user=user1)
session.add(color60)
session.commit()

color61 = Color(name="MEDIUMSEAGREEN", hex_code="#3CB371",
                rgb_code="RGB(60, 179, 113)", category=category6, user=user1)
session.add(color61)
session.commit()

color62 = Color(name="SEAGREEN", hex_code="#2E8B57",
                rgb_code="RGB(46, 139, 87)", category=category6, user=user1)
session.add(color62)
session.commit()

color63 = Color(name="FORESTGREEN", hex_code="#228B22",
                rgb_code="RGB(34, 139, 34)", category=category6, user=user1)
session.add(color63)
session.commit()

color64 = Color(name="GREEN", hex_code="#008000",
                rgb_code="RGB(0, 128, 0)", category=category6, user=user1)
session.add(color64)
session.commit()

color65 = Color(name="DARKGREEN", hex_code="#006400",
                rgb_code="RGB(0, 100, 0)", category=category6, user=user1)
session.add(color65)
session.commit()

color66 = Color(name="YELLOWGREEN", hex_code="#9ACD32",
                rgb_code="RGB(154, 205, 50)", category=category6, user=user1)
session.add(color66)
session.commit()

color67 = Color(name="OLIVEDRAB", hex_code="#6B8E23",
                rgb_code="RGB(107, 142, 35)", category=category6, user=user1)
session.add(color67)
session.commit()

color68 = Color(name="OLIVE", hex_code="#808000",
                rgb_code="RGB(128, 128, 0)", category=category6, user=user1)
session.add(color68)
session.commit()

color69 = Color(name="DARKOLIVEGREEN", hex_code="#556B2F",
                rgb_code="RGB(85, 107, 47)", category=category6, user=user1)
session.add(color69)
session.commit()

color70 = Color(name="MEDIUMAQUAMARINE", hex_code="#66CDAA",
                rgb_code="RGB(102, 205, 170)", category=category6, user=user1)
session.add(color70)
session.commit()

color71 = Color(name="DARKSEAGREEN", hex_code="#8FBC8B",
                rgb_code="RGB(143, 188, 139)", category=category6, user=user1)
session.add(color71)
session.commit()

color72 = Color(name="LIGHTSEAGREEN", hex_code="#20B2AA",
                rgb_code="RGB(32, 178, 170)", category=category6, user=user1)
session.add(color72)
session.commit()

color73 = Color(name="DARKCYAN", hex_code="#008B8B",
                rgb_code="RGB(0, 139, 139)", category=category6, user=user1)
session.add(color73)
session.commit()

color74 = Color(name="TEAL", hex_code="#008080",
                rgb_code="RGB(0, 128, 128)", category=category6, user=user1)
session.add(color74)
session.commit()

# BLUEs (25)

color75 = Color(name="AQUA", hex_code="#00FFFF",
                rgb_code="RGB(0, 255, 255)", category=category7, user=user1)
session.add(color75)
session.commit()

color76 = Color(name="CYAN", hex_code="#00FFFF",
                rgb_code="RGB(0, 255, 255)", category=category7, user=user1)
session.add(color76)
session.commit()

color77 = Color(name="LIGHTCYAN", hex_code="#E0FFFF",
                rgb_code="RGB(224, 255, 255)", category=category7, user=user1)
session.add(color77)
session.commit()

color78 = Color(name="PALETURQUOISE", hex_code="#AFEEEE",
                rgb_code="RGB(175, 238, 238)", category=category7, user=user1)
session.add(color78)
session.commit()

color79 = Color(name="AQUAMARINE", hex_code="#7FFFD4",
                rgb_code="RGB(127, 255, 212)", category=category7, user=user1)
session.add(color79)
session.commit()

color80 = Color(name="TURQUOISE", hex_code="#40E0D0",
                rgb_code="RGB(64, 224, 208)", category=category7, user=user1)
session.add(color80)
session.commit()

color81 = Color(name="MEDIUMTURQUOISE", hex_code="#48D1CC",
                rgb_code="RGB(72, 209, 204)", category=category7, user=user1)
session.add(color81)
session.commit()

color82 = Color(name="DARKTURQUOISE", hex_code="#00CED1",
                rgb_code="RGB(0, 206, 209)", category=category7, user=user1)
session.add(color82)
session.commit()

color83 = Color(name="CADETBLUE", hex_code="#5F9EA0",
                rgb_code="RGB(95, 158, 160)", category=category7, user=user1)
session.add(color83)
session.commit()

color84 = Color(name="STEELBLUE", hex_code="#4682B4",
                rgb_code="RGB(70, 130, 180)", category=category7, user=user1)
session.add(color84)
session.commit()

color85 = Color(name="LIGHTSTEELBLUE", hex_code="#B0C4DE",
                rgb_code="RGB(176, 196, 222)", category=category7, user=user1)
session.add(color85)
session.commit()

color86 = Color(name="POWDERBLUE", hex_code="#B0E0E6",
                rgb_code="RGB(176, 224, 230)", category=category7, user=user1)
session.add(color86)
session.commit()

color87 = Color(name="LIGHTBLUE", hex_code="#ADD8E6",
                rgb_code="RGB(173, 216, 230)", category=category7, user=user1)
session.add(color87)
session.commit()

color88 = Color(name="SKYBLUE", hex_code="#87CEEB",
                rgb_code="RGB(135, 206, 235)", category=category7, user=user1)
session.add(color88)
session.commit()

color89 = Color(name="LIGHTSKYBLUE", hex_code="#87CEFA",
                rgb_code="RGB(135, 206, 250)", category=category7, user=user1)
session.add(color89)
session.commit()

color90 = Color(name="DEEPSKYBLUE", hex_code="#00BFFF",
                rgb_code="RGB(0, 191, 255)", category=category7, user=user1)
session.add(color90)
session.commit()

color91 = Color(name="DODGERBLUE", hex_code="#1E90FF",
                rgb_code="RGB(30, 144, 255)", category=category7, user=user1)
session.add(color91)
session.commit()

color92 = Color(name="CORNFLOWERBLUE", hex_code="#6495ED",
                rgb_code="RGB(100, 149, 237)", category=category7, user=user1)
session.add(color92)
session.commit()

color93 = Color(name="MEDIUMSLATEBLUE", hex_code="#7B68EE",
                rgb_code="RGB(123, 104, 238)", category=category7, user=user1)
session.add(color93)
session.commit()

color94 = Color(name="ROYALBLUE", hex_code="#4169E1",
                rgb_code="RGB(65, 105, 225)", category=category7, user=user1)
session.add(color94)
session.commit()

color95 = Color(name="BLUE", hex_code="#0000FF",
                rgb_code="RGB(0, 0, 255)", category=category7, user=user1)
session.add(color95)
session.commit()

color96 = Color(name="MEDIUMBLUE", hex_code="#0000CD",
                rgb_code="RGB(0, 0, 205)", category=category7, user=user1)
session.add(color96)
session.commit()

color97 = Color(name="DARKBLUE", hex_code="#00008B",
                rgb_code="RGB(0, 0, 139)", category=category7, user=user1)
session.add(color97)
session.commit()

color98 = Color(name="NAVY", hex_code="#000080",
                rgb_code="RGB(0, 0, 128)", category=category7, user=user1)
session.add(color98)
session.commit()

color99 = Color(name="MIDNIGHTBLUE", hex_code="#191970",
                rgb_code="RGB(25, 25, 112)", category=category7, user=user1)
session.add(color99)
session.commit()

# BROWNs (17)

color100 = Color(name="CORNSILK", hex_code="#FFF8DC",
                 rgb_code="RGB(255, 248, 220)", category=category8, user=user1)
session.add(color100)
session.commit()

color101 = Color(name="BLANCHEDALMOND", hex_code="#FFEBCD",
                 rgb_code="RGB(255, 235, 205)", category=category8, user=user1)
session.add(color101)
session.commit()

color102 = Color(name="BISQUE", hex_code="#FFE4C4",
                 rgb_code="RGB(255, 228, 196)", category=category8, user=user1)
session.add(color102)
session.commit()

color103 = Color(name="NAVAJOWHITE", hex_code="#FFDEAD",
                 rgb_code="RGB(255, 222, 173)", category=category8, user=user1)
session.add(color103)
session.commit()

color104 = Color(name="WHEAT", hex_code="#F5DEB3",
                 rgb_code="RGB(245, 222, 179)", category=category8, user=user1)
session.add(color104)
session.commit()

color105 = Color(name="BURLYWOOD", hex_code="#DEB887",
                 rgb_code="RGB(222, 184, 135)", category=category8, user=user1)
session.add(color105)
session.commit()

color106 = Color(name="TAN", hex_code="#D2B48C",
                 rgb_code="RGB(210, 180, 140)", category=category8, user=user1)
session.add(color106)
session.commit()

color107 = Color(name="ROSYBROWN", hex_code="#BC8F8F",
                 rgb_code="RGB(188, 143, 143)", category=category8, user=user1)
session.add(color107)
session.commit()

color108 = Color(name="SANDYBROWN", hex_code="#F4A460",
                 rgb_code="RGB(244, 164, 96)", category=category8, user=user1)
session.add(color108)
session.commit()

color109 = Color(name="GOLDENROD", hex_code="#DAA520",
                 rgb_code="RGB(218, 165, 32)", category=category8, user=user1)
session.add(color109)
session.commit()

color110 = Color(name="DARKGOLDENROD", hex_code="#B8860B",
                 rgb_code="RGB(184, 134, 11)", category=category8, user=user1)
session.add(color110)
session.commit()

color111 = Color(name="PERU", hex_code="#CD853F",
                 rgb_code="RGB(205, 133, 63)", category=category8, user=user1)
session.add(color111)
session.commit()

color112 = Color(name="CHOCOLATE", hex_code="#D2691E",
                 rgb_code="RGB(210, 105, 30)", category=category8, user=user1)
session.add(color112)
session.commit()

color113 = Color(name="SADDLEBROWN", hex_code="#8B4513",
                 rgb_code="RGB(139, 69, 19)", category=category8, user=user1)
session.add(color113)
session.commit()

color114 = Color(name="SIENNA", hex_code="#A0522D",
                 rgb_code="RGB(160, 82, 45)", category=category8, user=user1)
session.add(color114)
session.commit()

color115 = Color(name="BROWN", hex_code="#A52A2A",
                 rgb_code="RGB(165, 42, 42)", category=category8, user=user1)
session.add(color115)
session.commit()

color115 = Color(name="MAROON", hex_code="#800000",
                 rgb_code="RGB(128, 0, 0)", category=category8, user=user1)
session.add(color115)
session.commit()

# WHITEs (17)

color116 = Color(name="WHITE", hex_code="#FFFFFF",
                 rgb_code="RGB(255, 255, 255)", category=category9, user=user1)
session.add(color116)
session.commit()

color117 = Color(name="SNOW", hex_code="#FFFAFA",
                 rgb_code="RGB(255, 250, 250)", category=category9, user=user1)
session.add(color117)
session.commit()

color118 = Color(name="HONEYDEW", hex_code="#F0FFF0",
                 rgb_code="RGB(240, 255, 240)", category=category9, user=user1)
session.add(color118)
session.commit()

color119 = Color(name="MINTCREAM", hex_code="#F5FFFA",
                 rgb_code="RGB(245, 255, 250)", category=category9, user=user1)
session.add(color119)
session.commit()

color120 = Color(name="AZURE", hex_code="#F0FFFF",
                 rgb_code="RGB(240, 255, 255)", category=category9, user=user1)
session.add(color120)
session.commit()

color121 = Color(name="ALICEBLUE", hex_code="#F0F8FF",
                 rgb_code="RGB(240, 248, 255)", category=category9, user=user1)
session.add(color121)
session.commit()

color122 = Color(name="GHOSTWHITE", hex_code="#F8F8FF",
                 rgb_code="RGB(248, 248, 255)", category=category9, user=user1)
session.add(color122)
session.commit()

color123 = Color(name="WHITESMOKE", hex_code="#F5F5F5",
                 rgb_code="RGB(245, 245, 245)", category=category9, user=user1)
session.add(color123)
session.commit()

color124 = Color(name="SEASHELL", hex_code="#FFF5EE",
                 rgb_code="RGB(255, 245, 238)", category=category9, user=user1)
session.add(color124)
session.commit()

color125 = Color(name="BEIGE", hex_code="#F5F5DC",
                 rgb_code="RGB(245, 245, 220)", category=category9, user=user1)
session.add(color125)
session.commit()

color126 = Color(name="OLDLACE", hex_code="#FDF5E6",
                 rgb_code="RGB(253, 245, 230)", category=category9, user=user1)
session.add(color126)
session.commit()

color127 = Color(name="FLORALWHITE", hex_code="#FFFAF0",
                 rgb_code="RGB(255, 250, 240)", category=category9, user=user1)
session.add(color127)
session.commit()

color128 = Color(name="IVORY", hex_code="#FFFFF0",
                 rgb_code="RGB(255, 255, 240)", category=category9, user=user1)
session.add(color128)
session.commit()

color129 = Color(name="ANTIQUEWHITE", hex_code="#FAEBD7",
                 rgb_code="RGB(250, 235, 215)", category=category9, user=user1)
session.add(color129)
session.commit()

color130 = Color(name="LINEN", hex_code="#FAF0E6",
                 rgb_code="RGB(250, 240, 230)", category=category9, user=user1)
session.add(color130)
session.commit()

color131 = Color(name="LAVENDERBLUSH", hex_code="#FFF0F5",
                 rgb_code="RGB(255, 240, 245)", category=category9, user=user1)
session.add(color131)
session.commit()

color132 = Color(name="MISTYROSE", hex_code="#FFE4E1",
                 rgb_code="RGB(255, 228, 225)", category=category9, user=user1)
session.add(color132)
session.commit()

# GRAYs (10)

color133 = Color(name="GAINSBORO", hex_code="#DCDCDC",
                 rgb_code="RGB(220, 220, 220)", category=category10, user=user1)
session.add(color133)
session.commit()

color134 = Color(name="LIGHTGRAY", hex_code="#D3D3D3",
                 rgb_code="RGB(211, 211, 211)", category=category10, user=user1)
session.add(color134)
session.commit()

color135 = Color(name="SILVER", hex_code="#C0C0C0",
                 rgb_code="RGB(192, 192, 192)", category=category10, user=user1)
session.add(color135)
session.commit()

color136 = Color(name="DARKGRAY", hex_code="#A9A9A9",
                 rgb_code="RGB(169, 169, 169)", category=category10, user=user1)
session.add(color136)
session.commit()

color137 = Color(name="GRAY", hex_code="#808080",
                 rgb_code="RGB(128, 128, 128)", category=category10, user=user1)
session.add(color137)
session.commit()

color138 = Color(name="DIMGRAY", hex_code="#696969",
                 rgb_code="RGB(105, 105, 105)", category=category10, user=user1)
session.add(color138)
session.commit()

color139 = Color(name="LIGHTSLATEGRAY", hex_code="#778899",
                 rgb_code="RGB(119, 136, 153)", category=category10, user=user1)
session.add(color139)
session.commit()

color140 = Color(name="SLATEGRAY", hex_code="#708090",
                 rgb_code="RGB(112, 128, 144)", category=category10, user=user1)
session.add(color140)
session.commit()

color141 = Color(name="DARKSLATEGRAY", hex_code="#2F4F4F",
                 rgb_code="RGB(47, 79, 79)", category=category10, user=user1)
session.add(color141)
session.commit()

color142 = Color(name="BLACK", hex_code="#000000",
                 rgb_code="RGB(0, 0, 0)", category=category10, user=user1)
session.add(color142)
session.commit()

print("added colors!")
