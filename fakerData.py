from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import choice
import string
from models.models import Users
from config import Config

# Créez une connexion à votre base de données
engine = create_engine(f"mysql+pymysql://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}")

conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

# Générez 1500 utilisateurs aléatoires
for _ in range(1500):
    name = ''.join(choice(string.ascii_letters) for _ in range(10))
    last_name = ''.join(choice(string.ascii_letters) for _ in range(10))
    first_name = ''.join(choice(string.ascii_letters) for _ in range(10))
    email = ''.join(choice(string.ascii_letters) for _ in range(10)) + '@example.com'
    phone = ''.join(choice(string.digits) for _ in range(10))
    password = ''.join(choice(string.ascii_letters + string.digits) for _ in range(10))

    user = Users(name=name, last_name=last_name, first_name=first_name, email=email, phone=phone, password=password)
    session.add(user)

# Validez les modifications
session.commit()

# Fermez la session
session.close()
