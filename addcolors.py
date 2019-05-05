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

print("added colors!")
