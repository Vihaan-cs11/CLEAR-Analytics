from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Float, String,Integer,create_engine
import os


#Connecting to the local database
BASE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

connect_str = "sqlite:///"+os.path.join(BASE_DIRECTORY,"user_analytics.db")

base = declarative_base()

session = sessionmaker()
"""
    class User
        id int
        username str
        email str
"""

engine = create_engine(connect_str,echo=True)

#Creating all the ORM classes, where the only fields included
#are the ones that are needed for the data analysis
class Users(base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key = True)
    user_name = Column(String(), nullable = False, unique = True)
    email = Column(String(), nullable = False, unique = True)
    location = Column(String())

class Products(base):
    __tablename__ = 'products'
    id = Column(Integer(), primary_key = True)
    product_name = Column(String(), nullable = False, unique = True)
    brand_id = Column(Integer(), nullable = False, unique = False)

class Product_Referrals(base):
    __tablename__ = 'product_refferals'
    id = Column(Integer(), primary_key = True)
    product_id = Column(Integer(), nullable = False, unique = False)
    price = Column(Float(), nullable = False)
    currency = Column(String(), nullable = False)
    #work on the backend code base and modify the dockerfile
    #start up the python server before using the rust server

class Brands(base):
    __tablename__ = 'brands'
    id = Column(Integer(), primary_key = True)
    name = Column(String(), nullable = False, unique = False)
    description = Column(String())
    created_by = Column(String())

class Posts(base):
    __tablename__ = 'posts'
    id = Column(Integer(), primary_key=True)
    author_id = Column(Integer(), nullable = False, unique = False)
    body_text = Column(String())
    products = Column(String())
    label = Column(String(), nullable = True)
    group_id = Column(String(), nullable = True)

class Routine_Checkins(base):
    __tablename__ = 'routine_checkins'
    id = Column(Integer(), primary_key=True)
    author_id = Column(Integer(), nullable = False)
    products_id = Column(String())
    #products_id is supposed to be an array type

class Groups(base):
    __tablename__ = 'groups'
    id = Column(Integer(), primary_key = True)
    name = Column(String(), nullable = False)
    tag_id = Column(Integer(), nullable = True)

class Tags(base):
    __tablename__ = 'tags'
    id = Column(Integer(), primary_key=True)
    tag = Column(String(), nullable = False, unique = True)
    description = Column(String(), nullable = True, unique = True)

class User_Tags(base):
    __tablename__ = 'user_tags'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), nullable = False)
    tags_id = Column(Integer(), nullable = False)
