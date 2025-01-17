from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    nfc_data: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = None



class NFCData(BaseModel):
    nfc_data: str

class User(BaseModel):
    name: str
    nfc_data: str

    class Config:
        orm_mode = True