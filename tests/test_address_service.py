import pytest
from unittest.mock import Mock
from app.services.address_service import AddressService
from app.models.models import Address

@pytest.fixture
def mock_db_session():
    mock = Mock()
    mock.get_all_address = Mock(return_value=[])  # Default return value as an empty list
    return mock

@pytest.fixture
def address_service(mock_db_session):
    return AddressService(db=mock_db_session)

@pytest.fixture
def sample_address():
    return Address(logradouro="Rua A")  # Adjust according to your Address model

def test_get_all_addresses(address_service, mock_db_session, sample_address):
    # Arrange
    mock_db_session.get_all_address.return_value = [sample_address]  # Ensure it returns a list
    
    # Act
    addresses = address_service.get_all_addresses()
    
    # Assert
    assert len(addresses) == 1
    assert addresses[0].logradouro == "Rua A"
