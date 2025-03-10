from django.contrib import admin
from django.urls import path, include

from boogiestats.boogie_ui.views import Handler404

urlpatterns = [
    path("", include("boogiestats.boogie_ui.urls")),
    path("", include("boogiestats.boogie_api.urls")),
    path("admin/", admin.site.urls),
]

handler404 = Handler404.as_view()
