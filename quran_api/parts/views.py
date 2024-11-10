""" API endpoints for quran_api.parts """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.parts.models import Part
from quran_api.parts.serializers import PartRetrieveSerializer, PartSerializer


# Create your views here.
class PartViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Parts (Juz) with filtering and sorting support"""

    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id"]
    filterset_fields = ["id"]

    def get_serializer_class(self):
        """Customize serializer_class based on self.action"""

        if self.action == "retrieve":
            self.serializer_class = PartRetrieveSerializer

        return super().get_serializer_class()
