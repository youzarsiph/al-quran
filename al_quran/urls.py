"""URLConf for al_quran"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from al_quran.comp.collections.views import CollectionViewSet
from al_quran.comp.items.views import ItemViewSet
from al_quran.comp.languages.views import LanguageViewSet
from al_quran.core.chapters.views import ChapterViewSet
from al_quran.core.groups.views import GroupViewSet
from al_quran.core.pages.views import PageViewSet
from al_quran.core.parts.views import PartViewSet
from al_quran.core.quarters.views import QuarterViewSet
from al_quran.core.verses.views import VerseViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("chapters", ChapterViewSet, "chapter")
router.register("parts", PartViewSet, "part")
router.register("groups", GroupViewSet, "group")
router.register("quarters", QuarterViewSet, "quarter")
router.register("pages", PageViewSet, "page")
router.register("verses", VerseViewSet, "verse")
router.register("languages", LanguageViewSet, "language")
router.register("collections", CollectionViewSet, "collection")
router.register("items", ItemViewSet, "item")


urlpatterns = [
    path("", include(router.urls)),
]
