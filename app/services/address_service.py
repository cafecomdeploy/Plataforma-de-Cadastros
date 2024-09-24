from app.repositories.address_repository import AddressRepository
from app.models.models import Address
from app.schemas.address_schema import AddressCreate
from typing import List, Optional
from sqlalchemy.orm import Session

class AddressService:
    def __init__(self, db: Session):
        self.repository = AddressRepository(db)

    def get_all_addresses(self) -> List[Address]:
        return self.repository.get_all_address()
    
    def get_address(self, address_id: int) -> Optional[Address]:
        return self.repository.get_by_id_addres(address_id)
    
    def get_address_by_user(self, usuario_id: int) -> Optional[List[Address]]:
        return self.repository.get_address_by_user(usuario_id)
    
    def create_address(self, address_create: AddressCreate) -> Address:
        return self.repository.create_address(address_create.dict())

    def update_user_address(self, address_id: int, address_data: dict):
        return self.repository.update_address(self, address_id, address_data)
