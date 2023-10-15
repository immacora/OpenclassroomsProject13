from django.shortcuts import render
from .models import Profile


def index(request):
    """
    View function for rendering a list of user profiles.

    Parameters:
        - request (HttpRequest): Current request object.

    Returns:
        HttpResponse: Renders the list of user profiles passed through the context dictionary.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    View function for rendering a user's profile.

    Parameters:
        - request (HttpRequest): Current request object.
        - username (str): The username of the user whose profile is to be displayed.

    Returns:
        HttpResponse: Renders the user's profile through the context dictionary.

    Raises:
        DoesNotExist: Raise a DoesNotExist exception
        if no user profile with the specified username is found.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
