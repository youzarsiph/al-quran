""" API endpoints for quran_api.pages """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from quran_api.pages.models import Page
from quran_api.pages.serializers import PageSerializer


# Create your views here.
class PageViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Pages"""

    queryset = Page.objects.select_related("chapter", "part", "group", "quarter")
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "verse_count"]
    filterset_fields = ["id", "chapter", "part", "group", "quarter", "verse_count"]
