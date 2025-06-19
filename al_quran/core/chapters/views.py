"""API endpoints for al_quran.core.chapters"""

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from al_quran.core.chapters.models import Chapter
from al_quran.core.chapters.serializers import ChapterSerializer


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
