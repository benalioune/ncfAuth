from sqlalchemy.orm import Session
import models, schemas, auth

def get_user_by_nfc_data(db: Session, nfc_data: str):
    return db.query(models.User).filter(models.User.nfc_data == nfc_data).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(name=user.name, nfc_data=user.nfc_data, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
