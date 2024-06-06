from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from faker import Faker
from main import engine, session

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
    phone = Column(String(50))
    password = Column(String(255)) 

# Créer les tables dans la base de données
Base.metadata.create_all(engine)

# Générez 1500 utilisateurs aléatoires avec Faker
fake = Faker()

for _ in range(100):
    username = fake.user_name()
    last_name = fake.last_name()
    first_name = fake.first_name()
    email = fake.email()
    phone = fake.phone_number()
    password = fake.password()

    user = Users(username=username, last_name=last_name, first_name=first_name, email=email, phone=phone, password=password)
    session.add(user)

# Validez les modifications
session.commit()

session.close()
