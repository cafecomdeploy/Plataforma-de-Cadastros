from sqlalchemy.orm import Session
from app.models.models import Address
from typing import List, Optional

class AddressRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_address(self) -> List[Address]:
        return self.db.query(Address).all()
    
    def get_by_id_addres(self, address_id: int) -> Optional[Address]:
        return self.db.query(Address).filter(Address.id == address_id).first()
    
    def get_address_by_user(self, usuario_id: int) -> Optional[List[Address]]:
        return self.db.query(Address).filter(Address.usuario_id == usuario_id).all()

    def create_address(self, address_data) -> Address:
        address = Address(**address_data)
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        return address

    def update_address(self, address_id: int, address_data: dict):
        address = self.db.query(Address).filter(Address.id == address_id).first()
        for key, value in address_data.items():
            setattr(address, key, value)
        self.db.commit()
        self.db.refresh(address)
        return address
    
    def delete_address(self, address_id: int) -> bool:
        address = self.db.query(Address).filter(Address.id == address_id).first()
        if address:
            self.db.delete(address)
            self.db.commit()
            return True
