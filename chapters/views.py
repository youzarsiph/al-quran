""" API endpoints for quran_api.chapters """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.chapters.models import Chapter
from quran_api.chapters.serializers import ChapterSerializer


# Create your views here.
class ChapterViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran chapters (Sura) with filtering and sorting support"""

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["id", "name", "type", "verse_count"]
    ordering_fields = ["id", "name", "verse_count"]
    search_fields = ["name", "translation", "transliteration"]
