""" API endpoints for al_quran.pages """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_quran.pages.models import Page
from al_quran.pages.serializers import PageSerializer


# Create your views here.
class PageViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Pages"""

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "verse_count", "created_at", "updated_at"]
    filterset_fields = ["id", "chapter", "part", "group", "quarter", "verse_count"]
