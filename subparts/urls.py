""" URLConf for quran_api.subparts """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quran_api.subparts.views import SubpartViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("subparts", SubpartViewSet, "subpart")

sub_router = DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path(
        "/<int:id>/",
        include((sub_router.urls, ""), namespace=""),
    ),
]
