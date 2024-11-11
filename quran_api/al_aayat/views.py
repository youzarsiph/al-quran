""" API endpoints for quran_api.al_aayat """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.al_aayat.models import Ayah
from quran_api.al_aayat.serializers import AyahSerializer


# Create your views here.
class VerseViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran aayat"""

    queryset = Ayah.objects.all()
    serializer_class = AyahSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["content"]
    ordering_fields = ["id", "number"]
    filterset_fields = [
        "id",
        "sura",
        "juz",
        "hizb",
        "riba",
        "safhah",
        "number",
        "content",
    ]
