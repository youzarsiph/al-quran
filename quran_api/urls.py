""" URLConf for quran_api """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quran_api.as_suwar.views import SuraViewSet
from quran_api.al_ahzab.views import HizbViewSet
from quran_api.as_safahat.views import SafhahViewSet
from quran_api.al_ajzaa.views import PartViewSet
from quran_api.al_arbaa.views import RibaViewSet
from quran_api.al_aayat.views import VerseViewSet

# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("al-aayat", VerseViewSet, "ayah")
router.register("al-ahzab", HizbViewSet, "hizb")
router.register("al-ajzaa", PartViewSet, "juz")
router.register("al-arbaa", RibaViewSet, "riba")
router.register("as-safahat", SafhahViewSet, "safhah")
router.register("as-suwar", SuraViewSet, "sura")


urlpatterns = [
    path("", include(router.urls)),
]
