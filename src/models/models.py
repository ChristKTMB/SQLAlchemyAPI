from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)