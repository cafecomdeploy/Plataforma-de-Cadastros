from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserResponse, LoginSchema
from app.services.user_service import create_user, authenticate_user
from app.auth.auth_handler import create_access_token
from app.database.session import get_db

router = APIRouter()

@router.post("/register/", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_data)
    return user

@router.post("/login/")
def login(login_data: LoginSchema, db: Session = Depends(get_db)):
    user = authenticate_user(db, login_data.email, login_data.senha)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
