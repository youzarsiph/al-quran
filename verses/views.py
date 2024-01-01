""" API endpoints for quran_api.verses """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.permissions import IsReadOnly
from quran_api.verses.models import Verse
from quran_api.verses.serializers import VerseSerializer


# Create your views here.
class VerseViewSet(ModelViewSet):
    """Create, view, update and delete"""

    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
    permission_classes = [IsAuthenticated, IsReadOnly]
    search_fields = ["text"]
    ordering_fields = ["id"]
    filterset_fields = ["text"]
