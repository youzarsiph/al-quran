"""URLConf for al_quran.comp"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from al_quran.comp.collections.views import CollectionViewSet
from al_quran.comp.items.views import ItemViewSet
from al_quran.comp.languages.views import LanguageViewSet

# Create your patterns here.
comp_router = DefaultRouter(trailing_slash=False)
comp_router.register("collections", CollectionViewSet, "collection")
comp_router.register("languages", LanguageViewSet, "language")
comp_router.register("items", ItemViewSet, "item")


urlpatterns = [
    path("", include(comp_router.urls)),
]
