""" URLConf for quran_api.pages """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quran_api.pages.views import PageViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("pages", PageViewSet, "page")

sub_router = DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path(
        "/<int:id>/",
        include((sub_router.urls, ""), namespace=""),
    ),
]
