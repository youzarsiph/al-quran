""" API endpoints for quran_api.pages """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.pages.models import Page
from quran_api.pages.serializers import PageSerializer


# Create your views here.
class PageViewSet(ReadOnlyModelViewSet):
    """Create, view, update and delete"""

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "verse_count"]
    filterset_fields = [
        "id",
        "chapter",
        "part",
        "verse_count",
        "created_at",
        "updated_at",
    ]
