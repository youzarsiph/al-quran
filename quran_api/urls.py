""" URLConf for quran_api """

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from quran_api.authors.views import AuthorViewSet
from quran_api.books.views import BookViewSet
from quran_api.chapters.views import ChapterViewSet
from quran_api.groups.views import GroupViewSet
from quran_api.items.views import ItemViewSet
from quran_api.languages.views import LanguageViewSet
from quran_api.pages.views import PageViewSet
from quran_api.parts.views import PartViewSet
from quran_api.quarters.views import QuarterViewSet
from quran_api.verses.views import VerseViewSet

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
