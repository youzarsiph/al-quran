""" API endpoints for quran_api.groups """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from quran_api.groups.models import Group
from quran_api.groups.serializers import GroupSerializer


# Create your views here.
class GroupViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Groups"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "verse_count"]
    filterset_fields = ["id", "part", "verse_count"]
