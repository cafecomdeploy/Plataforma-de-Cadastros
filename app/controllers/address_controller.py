from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.address_schema import AddressUpdate
from app.services.address_service import update_user_address
from app.database.session import get_db

router = APIRouter()

@router.put("/address/")
def update_address(address_data: AddressUpdate, db: Session = Depends(get_db)):
    updated_address = update_user_address(db, address_id=1, address_data=address_data.dict())  # Exemplo de id
    return updated_address
