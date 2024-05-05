""" URLConf for quran_api """

from django.urls import path, include


# Create your patterns here.
urlpatterns = [
    path("", include("quran_api.chapters.urls")),
    path("", include("quran_api.parts.urls")),
    path("", include("quran_api.groups.urls")),
    path("", include("quran_api.quarters.urls")),
    path("", include("quran_api.pages.urls")),
    path("", include("quran_api.verses.urls")),
]
