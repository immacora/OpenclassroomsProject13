from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("oc_lettings_site.urls")),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls"))
]
