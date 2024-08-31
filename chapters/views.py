""" API endpoints for quran_api.chapters """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.chapters.models import Chapter
from quran_api.chapters.serializers import ChapterRetrieveSerializer, ChapterSerializer


# Create your views here.
class ChapterViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran chapters (Sura) with filtering and sorting support"""

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["id", "name", "type", "order", "verse_count"]
    ordering_fields = ["id", "name", "order", "verse_count"]
    search_fields = ["name", "translation", "transliteration"]

    def get_serializer_class(self):
        """Customize serializer_class based on self.action"""

        if self.action == "retrieve":
            self.serializer_class = ChapterRetrieveSerializer

        return super().get_serializer_class()
