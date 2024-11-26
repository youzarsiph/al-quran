""" API endpoints for quran_api.languages """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from quran_api.languages.models import Language
from quran_api.languages.serializers import LanguageSerializer


# Create your views here.
class LanguageViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Translations"""

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["id", "name", "code"]
    ordering_fields = ["namer", "code"]
    search_fields = ["name", "code"]
