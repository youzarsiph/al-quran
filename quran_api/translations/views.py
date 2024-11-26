""" API endpoints for quran_api.translations """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from quran_api.translations.models import Translation
from quran_api.translations.serializers import TranslationSerializer


# Create your views here.
class TranslationViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Translations"""

    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["language", "chapter", "verse"]
    ordering_fields = ["chapter", "verse"]
    search_fields = ["content"]
