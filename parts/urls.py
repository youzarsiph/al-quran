""" URLConf for quran_api.parts """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quran_api.parts.views import PartViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("parts", PartViewSet, "part")

sub_router = DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path(
        "/<int:id>/",
        include((sub_router.urls, ""), namespace=""),
    ),
]
