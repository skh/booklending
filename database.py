from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///bookswapping.db')

class User(Base):
    __tablename__ = 'user'
    name = Column(String(80), nullable = False)
    email = Column(String(80), nullable = False)
    picture = Column(String(250))
    id = Column(Integer, primary_key = True)

class City(Base):
    __tablename__ = 'city'
    name = Column(
        String(80), nullable = False)
    id = Column(
        Integer, primary_key = True)
    user_id = Column(
        Integer, ForeignKey('user.id'))

class Book(Base):
    __tablename__ = 'book'
    title = Column(
        String(80), nullable = False)
    author = Column(
        String(80), nullable=False)
    description = Column(String(250))
    id = Column(
        Integer, primary_key = True)
    rcity_id = Column(
        Integer, ForeignKey('city.id'))
    book_id = Column(
        Integer, ForeignKey('book.id'))



Base.metadata.create_all(engine)
