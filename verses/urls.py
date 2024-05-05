""" URLConf for quran_api.verses """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quran_api.verses.views import VerseViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("verses", VerseViewSet, "verse")

urlpatterns = [
    path("", include(router.urls)),
]
