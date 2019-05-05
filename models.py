from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
            'user': self.user.name,
        }


class Color(Base):
    __tablename__ = 'color'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    hex_code = Column(String(250))
    rgb_code = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'hex_code': self.hex_code,
            'rgb_code': self.rgb_code,
            'category_id': self.category_id,
            'category': self.category.name,
            'user_id': self.user_id,
            'user': self.user.name,
        }


engine = create_engine('sqlite:///colors.db')


Base.metadata.create_all(engine)
