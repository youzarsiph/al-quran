""" API endpoints for quran_api.as_safahat """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.as_safahat.models import Safhah
from quran_api.as_safahat.serializers import SafhahSerializer


# Create your views here.
class SafhahViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Pages"""

    queryset = Safhah.objects.select_related("sura", "juz", "hizb", "riba")
    serializer_class = SafhahSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id"]
    filterset_fields = ["id", "sura", "juz", "hizb", "riba"]
