from sqlalchemy.orm import Session
from app.models.models import Address

def update_address(db: Session, address_id: int, address_data: dict):
    address = db.query(Address).filter(Address.id == address_id).first()
    for key, value in address_data.items():
        setattr(address, key, value)
    db.commit()
    db.refresh(address)
    return address
