from pydantic import BaseModel, constr

class AddressUpdate(BaseModel):
    logradouro: str
    cidade: str
    estado: str
    cep: constr(min_length=8, max_length=8)  # validação de CEP

    class Config:
        from_attributes = True
