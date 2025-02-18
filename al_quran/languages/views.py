"""API endpoints for al_quran.languages"""

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_quran.languages.models import Language
from al_quran.languages.serializers import LanguageSerializer


# Create your views here.
class LanguageViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Translations"""

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "code"]
    ordering_fields = ["namer", "code", "created_at", "updated_at"]
    filterset_fields = ["id", "name", "code"]
