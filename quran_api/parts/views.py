""" API endpoints for quran_api.parts """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from quran_api.parts.models import Part
from quran_api.parts.serializers import PartSerializer


# Create your views here.
class PartViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Part"""

    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "verse_count", "page_count", "created_at", "updated_at"]
    filterset_fields = ["id", "verse_count", "page_count"]
