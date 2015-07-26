from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///bookswapping.db')

class City(Base):
    __tablename__ = 'city'
    name = Column(
        String(80), nullable = False)
    id = Column(
        Integer, primary_key = True)

class Book(Base):
    __tablename__ = 'book'
    title = Column(
        String(80), nullable = False)
    author = Column(
        String(80), nullable=False)
    description = Column(String(250))
    id = Column(
        Integer, primary_key = True)


Base.metadata.create_all(engine)
