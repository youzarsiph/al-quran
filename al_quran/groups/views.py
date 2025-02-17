""" API endpoints for al_quran.groups """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_quran.groups.models import Group
from al_quran.groups.serializers import GroupSerializer


# Create your views here.
class GroupViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Groups"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["verse_count", "page_count", "created_at", "updated_at"]
    filterset_fields = ["id", "part", "verse_count", "page_count"]
