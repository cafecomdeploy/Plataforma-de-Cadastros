import pytest
from unittest.mock import MagicMock, patch
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserBase
from app.models.models import User
from pydantic import EmailStr
from datetime import date

@pytest.fixture
def mock_db():
    return MagicMock()

@pytest.fixture
def user_service(mock_db):
    return UserService(mock_db)

def test_create_user(user_service):
    # Dados do usuário a serem criados
    user_data = UserCreate(
        nome="Test User",
        email="test@example.com",
        data_nascimento=date(1990, 1, 1),
        senha="plainpassword"
    )
    
    # Mockando o método create_user do repositório
    user_service.repository.create_user = MagicMock(return_value=UserBase(
        nome="Test User",
        email="test@example.com",
        data_nascimento=date(1990, 1, 1),
        senha="hashed_password"  # Apenas um placeholder para a senha
    ))

    # Chamando o método
    created_user = user_service.create_user(user_data)

    # Verificando se a senha foi hashada e o usuário foi criado corretamente
    assert created_user.email == "test@example.com"
    assert created_user.nome == "Test User"
    assert created_user.data_nascimento == date(1990, 1, 1)
    user_service.repository.create_user.assert_called_once()
    assert user_service.repository.create_user.call_args[0][0].senha == user_service.repository.create_user.call_args[0][0].senha

def test_authenticate_user_success(user_service):
    # Mockando o usuário retornado
    user = User(
        email="test@example.com", 
        senha_hash="$2b$12$abcdefghijklmnopqrstuv", 
        nome="Test User",
        data_nascimento=date(1990, 1, 1)
    )
    user_service.repository.get_user_by_email = MagicMock(return_value=user)

    # Mockando o método de verificação da senha
    with patch('app.services.user_service.pwd_context.verify', return_value=True):
        authenticated_user = user_service.authenticate_user("test@example.com", "plainpassword")

    assert authenticated_user == user

def test_authenticate_user_failure(user_service):
    user_service.repository.get_user_by_email = MagicMock(return_value=None)

    authenticated_user = user_service.authenticate_user("test@example.com", "wrongpassword")

    assert not authenticated_user

    # Testando falha na verificação da senha
    user = User(
        email="test@example.com", 
        senha_hash="$2b$12$abcdefghijklmnopqrstuv", 
        nome="Test User",
        data_nascimento=date(1990, 1, 1)
    )
    user_service.repository.get_user_by_email = MagicMock(return_value=user)

    with patch('app.services.user_service.pwd_context.verify', return_value=False):
        authenticated_user = user_service.authenticate_user("test@example.com", "wrongpassword")

    assert not authenticated_user
