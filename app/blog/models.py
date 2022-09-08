# ###########import the ForeignKey

# from sqlalchemy import Column, Integer, String, ForeignKey

# from .database import Base

# #####################import the relationships#############
# from sqlalchemy.orm import relationship

# #################modles of tables#####################3
# class Blog(Base):
#     __tablename__ = 'blogs'
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     body = Column(String)
#     user_id = Column(Integer, ForeignKey('users.id'))
    
#     creator = relationship("User",back_populates="blogs")
    

# #############create the user paths in database
# class User(Base):
#     __tablename__ = 'users'
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String)
#     password = Column(String)
    
#     blogs = relationship('Blog', back_populates="creator")





from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")