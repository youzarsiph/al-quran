""" API endpoints for quran_api.parts """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.permissions import IsReadOnly
from quran_api.parts.models import Part
from quran_api.parts.serializers import PartSerializer


# Create your views here.
class PartViewSet(ModelViewSet):
    """Create, view, update and delete"""

    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated, IsReadOnly]
    search_fields = []
    ordering_fields = ["id"]
    filterset_fields = []
