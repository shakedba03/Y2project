from model import Base, Users, Blog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_blog(title, picture, name, text, day, month):
	blog_object = Blog(
	title = title,
	picture = picture,
	name = name,
	text = text,
	day = day,
	month = month)
	session.add(blog_object)
	session.commit()

def return_all_blogs():
	blogs = session.query(Blog).all()
	return blogs

def return_blog(id):
	session = DBSession()

	blog = session.query(Blog).filter_by(id = id).first()
	return blog



engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_user(username, password):
	user_object = Users(
	username = username,
	password = password)
	session.add(user_object)
	session.commit()

def return_all_users():
	session = DBSession()
	users = session.query(Users).all()
	return users

def return_user(username):
	session = DBSession()

	user = session.query(Users).filter_by(username = username).first()
	return user







