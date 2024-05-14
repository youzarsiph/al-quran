""" API endpoints for quran_api.pages """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.pages.models import Page
from quran_api.pages.serializers import PageSerializer


# Create your views here.
class PageViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Pages (Safhah) with filtering and sorting support"""

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "chapter", "part", "group", "quarter"]
    filterset_fields = ["id", "chapter", "part", "group", "quarter"]
