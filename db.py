import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import pandas as pd
from sqlalchemy import create_engine

# # Singleton to reuse the same connection across instances ## ifall vi skulle använda psycopg2 
# class Db:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(Db, cls).__new__(cls)
#             cls._instance.conn = cls._create_conn()
#         return cls._instance

#     @staticmethod
#     def _create_conn():
#         return psycopg2.connect(
#             dbname='bank',
#             user='postgres',
#             password='root',
#             host='localhost',
#             port='5432'
#         )

#     def get_conn(self):
#         return self.conn


Database_URL = "postgresql+psycopg2://k:9907@localhost:5432/postgres" # URL för att koppla till PostgreSQL databasen
engine = create_engine(Database_URL) # skapar en engine med SQLALchemy för att ansluta till databasen, denna engine hanterar alla olika operationer som man kan göra
SessionLocal = sessionmaker(bind=engine) # detta är en sessionmaker instans som tillåter att vi skapar session för våra olika interaktioner med databasoperationer

def init_db(): # funktion för att initialisera databasen genom de tabeller vi definerat i models.py (Base)
    Base.metadata.create_all(bind=engine)
    
