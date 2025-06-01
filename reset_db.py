from models import Base
from db import engine

# Droppar alla befintliga tabeller 
Base.metadata.drop_all(bind=engine)
print("Alla tabeller raderades.")

# Skapar om tabeller enligt modellerna igen 
Base.metadata.create_all(bind=engine)
print("Alla tabeller skapades igen enligt modellerna.")
