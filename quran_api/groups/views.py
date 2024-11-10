""" API endpoints for quran_api.groups """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.groups.models import Group
from quran_api.groups.serializers import GroupRetrieveSerializer, GroupSerializer


# Create your views here.
class GroupViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Groups (Hizbs) with filtering and sorting support"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "verse_count"]
    filterset_fields = ["id"]

    def get_serializer_class(self):
        """Customize serializer_class based on self.action"""

        if self.action == "retrieve":
            self.serializer_class = GroupRetrieveSerializer

        return super().get_serializer_class()
