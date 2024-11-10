""" API endpoints for quran_api.verses """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.verses.models import Verse
from quran_api.verses.serializers import VerseSerializer


# Create your views here.
class VerseViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran verses (ayah) with filtering and sorting support"""

    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["text", "transliteration"]
    ordering_fields = ["id", "number"]
    filterset_fields = [
        "id",
        "chapter",
        "part",
        "group",
        "quarter",
        "page",
        "number",
        "text",
    ]
