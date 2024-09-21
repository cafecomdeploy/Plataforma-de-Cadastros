from sqlalchemy.orm import Session
from app.models.models import User
class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data) -> User:
        user = User(
          nome=user_data.nome,
            email=user_data.email,
            senha_hash=user_data.senha,  
            data_nascimento=user_data.data_nascimento
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
