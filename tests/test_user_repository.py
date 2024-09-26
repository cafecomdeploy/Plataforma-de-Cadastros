import pytest
from unittest.mock import MagicMock
from app.models.models import User
from app.repositories.user_repository import UserRepository
from unittest.mock import ANY

@pytest.fixture
def mock_db():
    return MagicMock()

@pytest.fixture
def user_repository(mock_db):
    return UserRepository(mock_db)

def test_create_user(user_repository, mock_db):
    user_data = MagicMock()
    user_data.nome = "Teste"
    user_data.email = "teste@example.com"
    user_data.senha = "hashed_password"
    user_data.data_nascimento = "2000-01-01"

    user = user_repository.create_user(user_data)

    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

    assert user.nome == user_data.nome
    assert user.email == user_data.email
    assert user.senha_hash == user_data.senha
    assert user.data_nascimento == user_data.data_nascimento

def test_get_user_by_email(user_repository, mock_db):
    email = "teste@example.com"
    expected_user = User(nome="Teste", email=email, senha_hash="hashed_password", data_nascimento="2000-01-01")
    mock_db.query.return_value.filter.return_value.first.return_value = expected_user

    user = user_repository.get_user_by_email(email)

    mock_db.query.assert_called_once_with(User)
    mock_db.query.return_value.filter.assert_called_once_with(ANY)
    mock_db.query.return_value.filter.return_value.first.assert_called_once()

    assert user == expected_user
