""" API endpoints for quran_api.al_ahzab """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.al_ahzab.models import Hizb
from quran_api.al_ahzab.serializers import HizbSerializer


# Create your views here.
class HizbViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Hizbs"""

    queryset = Hizb.objects.all()
    serializer_class = HizbSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "verse_count"]
    filterset_fields = ["id"]
