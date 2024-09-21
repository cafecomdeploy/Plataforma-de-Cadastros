from pydantic import BaseModel, EmailStr, constr, Field
from datetime import date
from typing import List

class AddressBase(BaseModel):
    logradouro: str
    cidade: str
    estado: str
    cep: constr(min_length=8, max_length=8)  # validação de CEP

class UserBase(BaseModel):
    nome: str
    email: EmailStr
    data_nascimento: date

class UserCreate(UserBase):
    senha: constr(min_length=8)  # validação de senha

class UserResponse(UserBase):
    id: int
    enderecos: List[AddressBase] = []

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: EmailStr
    senha: str
