""" API endpoints for quran_api.subparts """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.permissions import IsReadOnly
from quran_api.subparts.models import Subpart
from quran_api.subparts.serializers import SubpartSerializer


# Create your views here.
class SubpartViewSet(ModelViewSet):
    """Create, view, update and delete"""

    queryset = Subpart.objects.all()
    serializer_class = SubpartSerializer
    permission_classes = [IsAuthenticated, IsReadOnly]
    search_fields = []
    ordering_fields = ["id"]
    filterset_fields = []
