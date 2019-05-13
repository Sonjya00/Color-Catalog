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
# REDs

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

# PINKs

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

# ORANGEs

color16 = Color(name="LIGHTSALMON", hex_code="#FFA07A",
                rgb_code="RGB(255, 160, 122)", category=category3, user=user1)
session.add(color16)
session.commit()

color17 = Color(name="CORAL", hex_code="#FF7F50",
                rgb_code="RGB(255, 127, 80)", category=category3, user=user1)
session.add(color17)
session.commit()

color18 = Color(name="TOMATO", hex_code="#FF6347",
                rgb_code="RGB(255, 99, 71)", category=category3, user=user1)
session.add(color18)
session.commit()

color19 = Color(name="ORANGERED", hex_code="#FF4500",
                rgb_code="RGB(255, 69, 0)", category=category3, user=user1)
session.add(color19)
session.commit()

color20 = Color(name="DARKORANGE", hex_code="#FF8C00",
                rgb_code="RGB(255, 140, 0)", category=category3, user=user1)
session.add(color20)
session.commit()

color21 = Color(name="ORANGE", hex_code="#FFA500",
                rgb_code="RGB(255, 165, 0)", category=category3, user=user1)
session.add(color21)
session.commit()

# YELLOWs

color22 = Color(name="GOLD", hex_code="#FFD700",
                rgb_code="RGB(255, 215, 0)", category=category4, user=user1)
session.add(color22)
session.commit()

color23 = Color(name="YELLOW", hex_code="#FFFF00",
                rgb_code="RGB(255, 255, 0)", category=category4, user=user1)
session.add(color23)
session.commit()

color24 = Color(name="LIGHTYELLOW", hex_code="#FFFFE0",
                rgb_code="RGB(255, 255, 224)", category=category4, user=user1)
session.add(color24)
session.commit()

color25 = Color(name="LEMONCHIFFON", hex_code="#FFFACD",
                rgb_code="RGB(255, 250, 205)", category=category4, user=user1)
session.add(color25)
session.commit()

color26 = Color(name="LIGHTGOLDENRODYELLOW", hex_code="#FAFAD2",
                rgb_code="RGB(250, 250, 210)", category=category4, user=user1)
session.add(color26)
session.commit()

color27 = Color(name="PAPAYAWHIP", hex_code="#FFEFD5",
                rgb_code="RGB(255, 239, 213)", category=category4, user=user1)
session.add(color27)
session.commit()

color28 = Color(name="MOCCASIN", hex_code="#FFE4B5",
                rgb_code="RGB(255, 228, 181)", category=category4, user=user1)
session.add(color28)
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

color31 = Color(name="DARKKHAKI", hex_code="#BDB76B",
                rgb_code="RGB(189, 183, 107)", category=category4, user=user1)
session.add(color31)
session.commit()

# PURPLEs

color32 = Color(name="LAVENDER", hex_code="#E6E6FA",
                rgb_code="RGB(230, 230, 250)", category=category5, user=user1)
session.add(color32)
session.commit()

color33 = Color(name="THISTLE", hex_code="#D8BFD8",
                rgb_code="RGB(216, 191, 216)", category=category5, user=user1)
session.add(color33)
session.commit()

color34 = Color(name="PLUM", hex_code="#DDA0DD",
                rgb_code="RGB(221, 160, 221)", category=category5, user=user1)
session.add(color34)
session.commit()

color35 = Color(name="VIOLET", hex_code="#EE82EE",
                rgb_code="RGB(238, 130, 238)", category=category5, user=user1)
session.add(color35)
session.commit()

color36 = Color(name="ORCHID", hex_code="#DA70D6",
                rgb_code="RGB(218, 112, 214)", category=category5, user=user1)
session.add(color36)
session.commit()

color37 = Color(name="FUCHSIA", hex_code="#FF00FF",
                rgb_code="RGB(255, 0, 255)", category=category5, user=user1)
session.add(color37)
session.commit()

color38 = Color(name="MAGENTA", hex_code="#FF00FF",
                rgb_code="RGB(255, 0, 255)", category=category5, user=user1)
session.add(color38)
session.commit()

color39 = Color(name="MEDIUMORCHID", hex_code="#BA55D3",
                rgb_code="RGB(186, 85, 211)", category=category5, user=user1)
session.add(color39)
session.commit()

color40 = Color(name="MEDIUMPURPLE", hex_code="#9370DB",
                rgb_code="RGB(147, 112, 219)", category=category5, user=user1)
session.add(color40)
session.commit()

print("added colors!")
