""" URLConf for al_quran """

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from al_quran.authors.views import AuthorViewSet
from al_quran.books.views import BookViewSet
from al_quran.chapters.views import ChapterViewSet
from al_quran.groups.views import GroupViewSet
from al_quran.items.views import ItemViewSet
from al_quran.languages.views import LanguageViewSet
from al_quran.pages.views import PageViewSet
from al_quran.parts.views import PartViewSet
from al_quran.quarters.views import QuarterViewSet
from al_quran.verses.views import VerseViewSet

# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("chapters", ChapterViewSet, "chapter")
router.register("parts", PartViewSet, "part")
router.register("groups", GroupViewSet, "group")
router.register("quarters", QuarterViewSet, "quarter")
router.register("pages", PageViewSet, "page")
router.register("verses", VerseViewSet, "verse")
router.register("authors", AuthorViewSet, "author")
router.register("books", BookViewSet, "book")
router.register("languages", LanguageViewSet, "language")
router.register("items", ItemViewSet, "item")


urlpatterns = [
    path("", include(router.urls)),
]
