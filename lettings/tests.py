import pytest
from django.core.exceptions import ValidationError

from .models import Address, Letting


@pytest.fixture
def valid_address_instance():
    address = Address.objects.create(
        number=1234,
        street="Main St",
        city="City",
        state="CA",
        zip_code=12345,
        country_iso_code="USA",
    )
    yield address
    address.delete()


@pytest.fixture
def valid_letting_instance(valid_address_instance):
    letting = Letting.objects.create(
        title="Test letting", address=valid_address_instance
    )
    yield letting
    letting.delete()


@pytest.mark.django_db
class TestAddressModel:
    """Unit tests for address model."""

    def test_create_address(self, valid_address_instance):
        """Tests address creation."""
        address = valid_address_instance
        address.save()
        assert Address.objects.count() == 1

    def test_address_str_method(self, valid_address_instance):
        """Tests if str method returns street number and name."""
        address = valid_address_instance
        assert str(address) == "1234 Main St"

    def test_number_validation(self):
        """Tests if address creation raise ValidationError with maximum value (9999) exceeded."""
        with pytest.raises(ValidationError):
            address = Address(
                number=10000,
                street="Main St",
                city="City",
                state="CA",
                zip_code=12345,
                country_iso_code="USA",
            )
            address.full_clean()

    def test_state_length_validation(self):
        """Tests if address creation raise ValidationError with less than 2 characters."""
        with pytest.raises(ValidationError):
            address = Address(
                number=1234,
                street="Main St",
                city="City",
                state="C",
                zip_code=12345,
                country_iso_code="USA",
            )
            address.full_clean()

    def test_zip_code_validation(self):
        """Tests if address creation raise ValidationError with maximum value (99999) exceeded."""
        with pytest.raises(ValidationError):
            address = Address(
                number=1234,
                street="Main St",
                city="City",
                state="CA",
                zip_code=100000,
                country_iso_code="USA",
            )
            address.full_clean()

    def test_country_iso_code_length_validation(self):
        """Tests if address creation raise ValidationError with less than 3 characters."""
        with pytest.raises(ValidationError):
            address = Address(
                number=1234,
                street="Main St",
                city="City",
                state="CA",
                zip_code=12345,
                country_iso_code="US",
            )
            address.full_clean()


@pytest.mark.django_db
class TestLettingModel:
    """Unit tests for letting model."""

    def test_create_letting(self, valid_address_instance):
        """Tests if str method returns letting title when creating letting."""
        letting = Letting.objects.create(
            title="Test Letting", address=valid_address_instance
        )
        assert str(letting) == "Test Letting"

    def test_letting_has_address(self, valid_address_instance):
        """Tests if location has a linked address."""
        letting = Letting.objects.create(
            title="Test Letting", address=valid_address_instance
        )
        assert letting.address == valid_address_instance
