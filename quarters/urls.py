""" URLConf for quran_api.quarters """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quran_api.quarters.views import QuarterViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("quarters", QuarterViewSet, "quarter")


urlpatterns = [
    path("", include(router.urls)),
]
