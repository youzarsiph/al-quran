""" API endpoints for quran_api.parts """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.parts.models import Part
from quran_api.parts.serializers import PartSerializer


# Create your views here.
class PartViewSet(ReadOnlyModelViewSet):
    """Create, view, update and delete"""

    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "verse_count"]
    filterset_fields = ["id"]
