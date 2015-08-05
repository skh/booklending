from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgres://uzpzbcmbkcdqhr:Bi9f0Q7OYDnb9AR3HiHBqwq8_S' +
                '@ec2-54-204-3-188.compute-1.amazonaws.com:5432/d7q2e' +
                'acsp9ckel'
                
Base = declarative_base() 
engine = create_engine(DATABASE_URL)

class User(Base):
    __tablename__ = 'appuser'   # 'user' is used internally by postgresql
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

class City(Base):
    __tablename__ = 'city'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('appuser.id'))
    books = relationship("Book")

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name
        }

class Book(Base):
    __tablename__ = 'book'
    title = Column(String(80), nullable=False)
    author = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey('city.id'))
    owner_id = Column(Integer, ForeignKey('appuser.id'))
    requestor_id = Column(Integer, ForeignKey('appuser.id'))
    requestor_comment = Column(String(400))
    status = Column(String(80), nullable=False)

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'author': self.author,
            'city_id' : self.city_id,
            'status' : self.status
        }


Base.metadata.create_all(engine)
