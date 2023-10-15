from django.shortcuts import render
from .models import Letting


def index(request):
    """
    View function for rendering a list of property lettings.

    Parameters:
        - request (HttpRequest): Current request object.

    Returns:
        HttpResponse: Renders the list of property lettings passed through the context dictionary.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    View function for displaying details of a property letting based on the provided letting_id.

    Parameters:
        - request (HttpRequest): Current request object.
        - letting_id (int): The unique identifier of the property letting to be displayed.

    Returns:
        HttpResponse: Renders the details of the property letting
        passed through the context dictionary.

    Raises:
        DoesNotExist: Raise a DoesNotExist exception
        if no property location with the specified letting_id is found.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
