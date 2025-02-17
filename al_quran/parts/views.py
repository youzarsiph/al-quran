""" API endpoints for al_quran.parts """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_quran.parts.models import Part
from al_quran.parts.serializers import PartSerializer


# Create your views here.
class PartViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Part"""

    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "verse_count", "page_count", "created_at", "updated_at"]
    filterset_fields = ["id", "verse_count", "page_count"]
