from fastapi import APIRouter, Depends, status,  HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserResponse, LoginSchema
from app.services.user_service import UserService
from app.auth.auth_handler import create_access_token
from app.database.session import get_db
from app.log import logger

router = APIRouter()

@router.post("/register/",status_code=status.HTTP_201_CREATED, response_model=UserResponse, description='Criando usuário')
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.create_user(user_data)
    return user

@router.post("/login/", status_code=status.HTTP_201_CREATED, description='Realizando login')
async def login(login_data: LoginSchema, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.authenticate_user(login_data.email, login_data.senha)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer",  "user_id": user.id }
