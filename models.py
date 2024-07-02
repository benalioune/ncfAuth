from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)  # Ajout de la longueur maximale
    nfc_data = Column(String(50), unique=True, index=True)  # Ajout de la longueur maximale
    hashed_password = Column(String(100))  # Ajout de la longueur maximale
