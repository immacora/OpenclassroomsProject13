from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("oc_lettings_site.urls")),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
]

handler404 = "oc_lettings_site.views.custom_404_view"  # noqa F811
handler500 = "oc_lettings_site.views.custom_500_view"  # noqa F811
