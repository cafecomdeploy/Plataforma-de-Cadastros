from pydantic import BaseModel, constr

class AddressBase(BaseModel):
    logradouro: str
    cidade: str
    estado: str
    cep: str

class AddressCreate(AddressBase):
    usuario_id: int
class AddressUpdate(BaseModel):
    logradouro: str
    cidade: str
    estado: str
    cep: constr(min_length=8, max_length=8)  # validação de CEP

    class Config:
        from_attributes = True
