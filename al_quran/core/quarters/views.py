"""API endpoints for al_quran.core.quarters"""

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from al_quran.core.quarters.models import Quarter
from al_quran.core.quarters.serializers import QuarterSerializer


# Create your views here.
class QuarterViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran arbaa"""

    queryset = Quarter.objects.all()
    serializer_class = QuarterSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "verse_count", "page_count", "created_at", "updated_at"]
    filterset_fields = ["id", "group", "verse_count", "page_count"]
