from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"User(name='{self.name}', last_name='{self.last_name}', first_name='{self.first_name}', email='{self.email}', phone='{self.phone}', password='{self.password}')"