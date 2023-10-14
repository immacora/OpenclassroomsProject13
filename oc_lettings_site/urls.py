from django.urls import path

from .views import index

app_name = "oc_lettings_site"


urlpatterns = [
    path("", index, name="index")
]
