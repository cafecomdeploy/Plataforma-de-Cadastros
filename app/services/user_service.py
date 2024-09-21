from passlib.context import CryptContext
from app.repositories.user_repository import UserRepository
from app.models.models import User
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserBase, UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, user_data: UserCreate) -> UserBase:
        senha_hash = pwd_context.hash(user_data.senha)
        user_data.senha = senha_hash
        return self.repository.create_user(user_data)

    def authenticate_user(self, email: str, senha: str):
        user = self.repository.get_user_by_email(email)
        if not user or not pwd_context.verify(senha, user.senha_hash):
            return False
        return user
