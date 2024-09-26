from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.address_schema import AddressUpdate, AddressCreate, AddressBase
from app.services.address_service import AddressService
from app.database.session import get_db
from app.auth.auth_handler import get_current_user
from typing import List, Optional

router = APIRouter()

@router.get("/address", response_model= List[AddressBase])
async def get_address(db: Session = Depends(get_db)) -> AddressBase:
    address_service = AddressService(db)
    address = address_service.get_all_addresses()
    return address

@router.get("/address/{address_id}")
async def get_by_id_address( address_id: int, db: Session = Depends(get_db)) -> AddressCreate:
    address_service = AddressService(db)
    address = address_service.get_address(address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Endereço não localizado")
    return address

@router.get("/address-user/{usuario_id}")
async def get_address_by_Userid(usuario_id: int, db: Session = Depends(get_db),  current_user: dict = Depends(get_current_user) ) -> List[AddressBase]:
    address_service = AddressService(db)
    addresses = address_service.get_address_by_user(usuario_id)
    print(addresses)
    if addresses is None:  # Se não houver endereços cadastrados, return None
        raise HTTPException(status_code=404, detail="Usuário não possui cadastro")
    
    return addresses

@router.post("/cadastro/address/",  description= "Cadastro de Endereço")
async def register_address(address_data: AddressCreate, db: Session = Depends(get_db),  current_user: dict = Depends(get_current_user) ):
    service = AddressService(db)
    return service.create_address(address_data)

@router.put("/address/{address_id}", description="Editando Endereço")
async def update_address(address_id: int, address_data: AddressUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = AddressService(db)
    updated_address = service.update_user_address(address_id=address_id, address_data=address_data.dict()) 
    return updated_address

@router.delete("/addresses/{address_id}", response_model=dict)
def remove_address(address_id: int, db: Session = Depends(get_db),  current_user: dict = Depends(get_current_user) ):
    address_service = AddressService(db)
    success = address_service.delete_address(address_id)
    if not success:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return {"detail": "Endereço deletado com sucesso"}
