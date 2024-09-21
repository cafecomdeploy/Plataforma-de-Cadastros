from app.repositories import address_repository
from sqlalchemy.orm import Session

def update_user_address(db: Session, address_id: int, address_data: dict):
    return address_repository.update_address(db, address_id, address_data)
