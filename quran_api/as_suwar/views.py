""" API endpoints for quran_api.as_suwar """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.as_suwar.models import Sura
from quran_api.as_suwar.serializers import SuraSerializer


# Create your views here.
class SuraViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Sura"""

    queryset = Sura.objects.all()
    serializer_class = SuraSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["id", "name", "type", "order", "verse_count"]
    ordering_fields = ["id", "name", "order", "verse_count"]
    search_fields = ["name"]
