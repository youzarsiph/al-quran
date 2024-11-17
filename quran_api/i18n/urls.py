""" URLConf for Quran API I18N """

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from quran_api.i18n.languages.views import LanguageViewSet
from quran_api.i18n.translations.views import TranslationViewSet
from quran_api.i18n.transliterations.views import TransliterationViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("languages", LanguageViewSet, "language")
router.register("translations", TranslationViewSet, "translation")
router.register("transliterations", TransliterationViewSet, "transliteration")


urlpatterns = [
    path("", include(router.urls)),
]
