from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Users(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key = True)
	username = Column(String)
	password = Column(String)

class Blog(Base):
	__tablename__ = 'blog'
	id = Column(Integer, primary_key = True)
	title = Column(String)
	picture = Column(String)
	name = Column(String)
	text = Column(String)
	day = Column(String)
	month = Column(String)
		