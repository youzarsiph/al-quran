""" URLConf for quran_api """

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from quran_api.chapters.views import ChapterViewSet
from quran_api.groups.views import GroupViewSet
from quran_api.languages.views import LanguageViewSet
from quran_api.pages.views import PageViewSet
from quran_api.parts.views import PartViewSet
from quran_api.quarters.views import QuarterViewSet
from quran_api.translations.views import TranslationViewSet
from quran_api.transliterations.views import TransliterationViewSet
from quran_api.verses.views import VerseViewSet

# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("verses", VerseViewSet, "verse")
router.register("groups", GroupViewSet, "group")
router.register("languages", LanguageViewSet, "language")
router.register("parts", PartViewSet, "part")
router.register("quarters", QuarterViewSet, "quarter")
router.register("pages", PageViewSet, "page")
router.register("translations", TranslationViewSet, "translation")
router.register("transliterations", TransliterationViewSet, "transliteration")
router.register("chapters", ChapterViewSet, "chapter")


urlpatterns = [
    path("", include(router.urls)),
]
