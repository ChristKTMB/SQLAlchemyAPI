from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from random import choice
from main import engine, session
import string

# Créer une instance de Base
Base = declarative_base()

# Définir le modèle Users
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255)) 
    last_name = Column(String(255)) 
    first_name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(20))
    password = Column(String(255)) 

# Créer les tables dans la base de données
Base.metadata.create_all(engine)

# Générez 1500 utilisateurs aléatoires
for _ in range(20):
    username = ''.join(choice(string.ascii_letters) for _ in range(10))
    last_name = ''.join(choice(string.ascii_letters) for _ in range(10))
    first_name = ''.join(choice(string.ascii_letters) for _ in range(10))
    email = ''.join(choice(string.ascii_letters) for _ in range(10)) + '@example.com'
    phone = ''.join(choice(string.digits) for _ in range(10))
    password = ''.join(choice(string.ascii_letters + string.digits) for _ in range(10))

    user = Users(username=username, last_name=last_name, first_name=first_name, email=email, phone=phone, password=password)
    session.add(user)

# Validez les modifications
session.commit()

session.close()