from django.shortcuts import render
import logging

from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    View function for rendering a list of user profiles.

    Parameters:
        - request (HttpRequest): Current request object.

    Returns:
        HttpResponse: Renders the list of user profiles passed through the context dictionary
        or custom 500 page.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)
    except Exception as e:
        logger.error(f"Error fetching profiles: {e}")
        return render(request, "500.html", status=500)


def profile(request, username):
    """
    View function for rendering a user's profile.

    Parameters:
        - request (HttpRequest): Current request object.
        - username (str): The username of the user whose profile is to be displayed.

    Returns:
        HttpResponse: Renders the user's profile through the context dictionary or custom 404 page.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except Profile.DoesNotExist:
        logger.error(f"Profile for username {username} not found.")
        return render(request, "404.html", status=404)
