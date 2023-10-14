from django.shortcuts import render


def index(request):
    return render(request, 'oc_lettings_site/index.html')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def custom_500_view(request):
    return render(request, '500.html', status=500)
