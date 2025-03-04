"""API endpoints for al_quran.core.verses"""

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_quran.core.verses.models import Verse
from al_quran.core.verses.serializers import VerseSerializer


# Create your views here.
class VerseViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran verses"""

    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["content"]
    ordering_fields = ["number", "created_at", "updated_at"]
    filterset_fields = ["id", "chapter", "part", "group", "quarter", "page", "number"]
