"""API endpoints for al_quran.chapters"""

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_quran.chapters.models import Chapter
from al_quran.chapters.serializers import ChapterSerializer


# Create your views here.
class ChapterViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Chapter"""

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name"]
    ordering_fields = [
        "name",
        "order",
        "verse_count",
        "page_count",
        "created_at",
        "updated_at",
    ]
    filterset_fields = ["id", "name", "type", "order", "verse_count", "page_count"]
