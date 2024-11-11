""" API endpoints for quran_api.al_ajzaa """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.al_ajzaa.models import Juz
from quran_api.al_ajzaa.serializers import JuzSerializer


# Create your views here.
class PartViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Juz"""

    queryset = Juz.objects.all()
    serializer_class = JuzSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id"]
    filterset_fields = ["id"]
