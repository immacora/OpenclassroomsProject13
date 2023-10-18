from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    View function for rendering the index page of the website.

    Parameters:
        - request (HttpRequest): Current request object.

    Returns:
        HttpResponse: Renders the index page HTML template or custom 500 page.
    """
    try:
        return render(request, "oc_lettings_site/index.html")
    except Exception as e:
        logger.error(f"Error rendering index page: {e}")
        return render(request, "500.html", status=500)


def custom_404_view(request, exception):
    """
    View function for rendering a custom 404 error page.

    Parameters:
        - request (HttpRequest): Current request object.
        - exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: Renders a custom 404 error page HTML template with a status code of 404.
    """
    return render(request, "404.html", status=404)


def custom_500_view(request):
    """
    View function for rendering a custom 500 error page.

    Parameters:
        - request (HttpRequest): Current request object.

    Returns:
        HttpResponse: Renders a custom 500 error page HTML template with a status code of 500.
    """
    return render(request, "500.html", status=500)
