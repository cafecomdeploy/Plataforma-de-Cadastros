from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String)
    data_nascimento = Column(Date)

    enderecos = relationship("Address", back_populates="usuario")

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('users.id'))
    logradouro = Column(String)
    cidade = Column(String)
    estado = Column(String)
    cep = Column(String)

    usuario = relationship("User", back_populates="enderecos")
