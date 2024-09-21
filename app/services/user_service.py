from passlib.context import CryptContext
from app.repositories import user_repository
from app.models.models import User
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user_data):
    senha_hash = pwd_context.hash(user_data.senha)
    db_user = User(
        nome=user_data.nome,
        email=user_data.email,
        senha_hash=senha_hash,
        data_nascimento=user_data.data_nascimento
    )
    return user_repository.create_user(db, db_user)

def authenticate_user(db: Session, email: str, senha: str):
    user = user_repository.get_user_by_email(db, email)
    if not user or not pwd_context.verify(senha, user.senha_hash):
        return False
    return user
