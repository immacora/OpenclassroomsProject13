from django.shortcuts import render
import logging

from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """
    View function for rendering a list of property lettings.

    Parameters:
        - request (HttpRequest): Current request object.

    Returns:
        HttpResponse: Renders the list of property lettings passed through the context dictionary
        or custom 500 page.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {"lettings_list": lettings_list}
        return render(request, "lettings/index.html", context)
    except Exception as e:
        logger.error(f"Error fetching lettings: {e}")
        return render(request, "500.html", status=500)


def letting(request, letting_id):
    """
    View function for displaying details of a property letting based on the provided letting_id.

    Parameters:
        - request (HttpRequest): Current request object.
        - letting_id (int): The unique identifier of the property letting to be displayed.

    Returns:
        HttpResponse: Renders the details of the property letting
        passed through the context dictionary or custom 404 page.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Letting.DoesNotExist:
        logger.error(f"Letting with ID {letting_id} not found.")
        return render(request, "404.html", status=404)
