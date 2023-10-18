import pytest
from django.core.exceptions import ValidationError
from django.db.utils import OperationalError
from django.urls import reverse

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


@pytest.mark.django_db
class TestIndexLettingsView:
    """Integration tests for lettings index view."""

    def test_index_view(self, client, valid_letting_instance):
        """
        GIVEN a fixture for valid_letting_instance with title and linked address
        WHEN the '/lettings' page is requested (GET)
        THEN checks that response is 200, the correct template is used and title is displayed
        """
        url = reverse("lettings:index")
        response = client.get(url)
        assert response.status_code == 200
        assert "lettings/index.html" in [
            template.name for template in response.templates
        ]
        assert valid_letting_instance.title in str(response.content)

    def test_index_view_with_no_lettings(self, client):
        """
        GIVEN no lettings exist in the database
        WHEN the '/lettings' page is requested (GET)
        THEN checks that response is 200,
        the correct template is used, Lettings title and message are displayed
        """
        url = reverse("lettings:index")
        response = client.get(url)
        assert response.status_code == 200
        assert "lettings/index.html" in [
            template.name for template in response.templates
        ]
        assert "Lettings" in str(response.content)
        assert "No lettings are available." in str(response.content)

    def test_index_view_with_error_500(self, client, mocker):
        """
        GIVEN a wrong mock for database lettings list
        WHEN the '/lettings' page is requested (GET)
        THEN checks that response is 500 and the custom error template is used
        """
        mocker.patch(
            "lettings.models.Letting.objects.all", side_effect=OperationalError
        )
        url = reverse("lettings:index")
        response = client.get(url)
        assert response.status_code == 500
        assert "500.html" in [template.name for template in response.templates]
        assert "INTERNAL SERVER ERROR" in str(response.content)


@pytest.mark.django_db
class TestLettingView:
    """Integration tests for letting view."""

    def test_letting_view(self, client, valid_letting_instance):
        """
        GIVEN a fixture for valid_letting_instance with title and linked address
        WHEN the '/lettings/letting' page is requested (GET)
        THEN checks that response is 200, the correct template is used
        and letting details are displayed
        """
        url = reverse("lettings:letting", args=[valid_letting_instance.id])
        response = client.get(url)
        assert response.status_code == 200
        assert "lettings/letting.html" in [
            template.name for template in response.templates
        ]
        assert valid_letting_instance.title in str(response.content)
        assert str(valid_letting_instance.address) in str(response.content)

    def test_letting_view_not_found(self, client):
        """
        GIVEN wrong letting
        WHEN the '/lettings/letting' page is requested (GET)
        THEN checks that response is 404 and the custom template is rendered
        """
        response = client.get("lettings/9999/")
        assert response.status_code == 404
        assert "404.html" in [template.name for template in response.templates]
        assert "PAGE NOT FOUND" in str(response.content)
