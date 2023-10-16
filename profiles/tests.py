import pytest
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.urls import reverse

from .models import Profile


@pytest.fixture
def valid_profile_instance():
    valid_user = User.objects.create_user(username="testuser", password="123456789!")
    profile = Profile.objects.create(
        user=valid_user, favorite_city="Test favorite city name"
    )
    yield profile
    profile.delete()


@pytest.mark.django_db
class TestProfileModel:
    """Unit tests for profile model."""

    def test_create_profile(self, valid_profile_instance):
        """Tests profile creation."""
        profile = valid_profile_instance
        profile.save()
        assert Profile.objects.count() == 1

    def test_profile_str_method(self, valid_profile_instance):
        """Tests if str method returns username."""
        profile = valid_profile_instance
        assert str(profile) == profile.user.username

    def test_create_profile_with_no_favorite_city(self):
        """Tests if profile creation works with no favorite city."""
        valid_user = User.objects.create_user(
            username="testuser", password="123456789!"
        )
        profile = Profile.objects.create(user=valid_user, favorite_city="")
        profile.save()
        assert Profile.objects.count() == 1

    def test_create_profile_with_no_user(self):
        """Tests if profile creation failed with no user."""
        with pytest.raises(IntegrityError):
            Profile.objects.create(user=None, favorite_city="Test favorite city name")


@pytest.mark.django_db
class TestIndexProfilesView:
    """Integration tests for profiles index view."""

    def test_index_view(self, client, valid_profile_instance):
        """
        GIVEN a fixture for valid_profile_instance with favorite city and linked user
        WHEN the '/profiles' page is requested (GET)
        THEN checks that response is 200, the correct template is used
        and username is displayed
        """
        url = reverse("profiles:index")
        response = client.get(url)
        assert response.status_code == 200
        assert "profiles/index.html" in [
            template.name for template in response.templates
        ]
        assert valid_profile_instance.user.username in str(response.content)

    def test_index_view_no_profiles(self, client):
        """
        GIVEN no profiles exist in the database
        WHEN the '/profiles' page is requested (GET)
        THEN checks that response is 200,
        the correct template is used, Profiles title and message are displayed
        """
        url = reverse("profiles:index")
        response = client.get(url)
        assert response.status_code == 200
        assert "profiles/index.html" in [
            template.name for template in response.templates
        ]
        assert "Profiles" in str(response.content)
        assert "No profiles are available." in str(response.content)


@pytest.mark.django_db
class TestProfileView:
    """Integration tests for profile view."""

    def test_profile_view(self, client, valid_profile_instance):
        """
        GIVEN a fixture for valid_profile_instance with favorite city and linked user
        WHEN the '/profiles/profile' page is requested (GET)
        THEN checks that response is 200, the correct template is used
        and profile details are displayed
        """
        url = reverse("profiles:profile", args=[valid_profile_instance.user.username])
        response = client.get(url)
        assert response.status_code == 200
        assert "profiles/profile.html" in [
            template.name for template in response.templates
        ]
        assert str(valid_profile_instance.user.username) in str(response.content)
        assert str(valid_profile_instance.user.first_name) in str(response.content)
        assert str(valid_profile_instance.user.last_name) in str(response.content)
        assert str(valid_profile_instance.user.email) in str(response.content)
        assert str(valid_profile_instance.favorite_city) in str(response.content)

    def test_profile_view_not_profile(self, client):
        """
        GIVEN no profile exist in the database
        WHEN the '/profiles/profile' page is requested (GET)
        THEN checks that response is 404
        """
        response = client.get("profiles/WRONG-ID/")
        assert response.status_code == 404
