from sqlalchemy import CHAR, Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)
    
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(CHAR, index=True)
    surname = Column(CHAR, index=True)
    bod = Column(CHAR, index=True)
    sex = Column(CHAR, index=True)
    age = Column(Integer, index=True)

