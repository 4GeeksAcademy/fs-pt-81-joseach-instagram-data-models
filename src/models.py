import os
import sys
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False, unique=True)
    
    followers = relationship("Follower", backref="user")
    posts = relationship("Post", backref='user')
    comments = relationship("Comment", backref="author")

class Follower(Base):
    __tablename__ = 'follower'
    
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    comments = relationship('Comment', backref="post")
    media = relationship('Media', backref='post')

class Comment(Base):
    __tablename__ = 'comment'
    
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

render_er(Base, 'diagram.png')
