import pytest
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

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
