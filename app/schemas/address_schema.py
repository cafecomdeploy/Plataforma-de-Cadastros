from pydantic import BaseModel, constr

class AddressBase(BaseModel):
    id: int
    logradouro: str
    cidade: str
    estado: str
    cep: str
class AddressCreate(AddressBase):
    usuario_id: int
class AddressUpdate(BaseModel):
    id: int
    logradouro: str
    cidade: str
    estado: str
    cep: str
    class Config:
        from_attributes = True
