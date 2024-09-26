import pytest
from unittest.mock import MagicMock
from app.models.models import Address
from app.schemas.address_schema import AddressBase
from app.repositories.address_repository import AddressRepository

@pytest.fixture
def mock_db():
    return MagicMock()

@pytest.fixture
def address_repository(mock_db):
    return AddressRepository(mock_db)

def test_get_all_address(address_repository, mock_db):
    expected_addresses = [
        Address(logradouro="Rua A", cidade="Cidade A", estado="Estado A", cep="12345678"),
        Address(logradouro="Rua B", cidade="Cidade B", estado="Estado B", cep="87654321")
    ]
    mock_db.query.return_value.all.return_value = expected_addresses

    addresses = address_repository.get_all_address()

    mock_db.query.assert_called_once_with(Address)
    mock_db.query.return_value.all.assert_called_once()

    assert addresses == expected_addresses

def test_get_by_id_address_success(address_repository, mock_db):
    expected_address = Address(logradouro="Rua A", cidade="Cidade A", estado="Estado A", cep="12345678")  
    mock_db.query.return_value.filter.return_value.first.return_value = expected_address

    address = address_repository.get_by_id_addres(1)

    assert address is not None
    assert address.id == expected_address.id
    assert address.cidade == expected_address.cidade
    assert address.cep == expected_address.cep

    mock_db.query.assert_called_once_with(Address)
    mock_db.query.return_value.filter.assert_called_once()
    

def test_delete_address_not_found(address_repository, mock_db):
    address_id = 1
    mock_db.query.return_value.filter.return_value.first.return_value = None
    success = address_repository.delete_address(address_id)
    mock_db.query.assert_called_once_with(Address)
    mock_db.query.return_value.filter.assert_called_once()  

    assert success is False
