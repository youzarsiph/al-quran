""" API endpoints for quran_api.al_arbaa """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.al_arbaa.models import Riba
from quran_api.al_arbaa.serializers import RibaSerializer


# Create your views here.
class RibaViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran arbaa"""

    queryset = Riba.objects.all()
    serializer_class = RibaSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id"]
    filterset_fields = ["id", "name"]
