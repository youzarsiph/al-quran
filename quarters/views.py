""" API endpoints for quran_api.quarters """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.quarters.models import Quarter
from quran_api.quarters.serializers import QuarterSerializer


# Create your views here.
class QuarterViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran quarters (Hizb quarter) with filtering and sorting support"""

    queryset = Quarter.objects.all()
    serializer_class = QuarterSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "verse_count"]
    filterset_fields = ["id"]
