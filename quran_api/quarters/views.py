""" API endpoints for quran_api.quarters """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.quarters.models import Quarter
from quran_api.quarters.serializers import QuarterRetrieveSerializer, QuarterSerializer


# Create your views here.
class QuarterViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran group quarters (Hizb quarters) with filtering and sorting support"""

    queryset = Quarter.objects.all()
    serializer_class = QuarterSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id"]
    filterset_fields = ["id"]

    def get_serializer_class(self):
        """Customize serializer_class based on self.action"""

        if self.action == "retrieve":
            self.serializer_class = QuarterRetrieveSerializer

        return super().get_serializer_class()
