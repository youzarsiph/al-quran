"""URLConf for al_quran.i18n"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from al_quran.i18n.authors.views import AuthorViewSet
from al_quran.i18n.books.views import BookViewSet
from al_quran.i18n.items.views import ItemViewSet
from al_quran.i18n.languages.views import LanguageViewSet

# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("authors", AuthorViewSet, "author")
router.register("books", BookViewSet, "book")
router.register("languages", LanguageViewSet, "language")
router.register("items", ItemViewSet, "item")


urlpatterns = [
    path("", include(router.urls)),
]
