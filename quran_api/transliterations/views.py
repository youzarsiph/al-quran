""" API endpoints for quran_api.transliterations """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from quran_api.transliterations.models import Transliteration
from quran_api.transliterations.serializers import TransliterationSerializer


# Create your views here.
class TransliterationViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Transliterations"""

    queryset = Transliteration.objects.all()
    serializer_class = TransliterationSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["language", "chapter", "verse"]
    ordering_fields = ["chapter", "verse"]
    search_fields = ["content"]
