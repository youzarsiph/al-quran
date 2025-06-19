"""API endpoints for al_quran.comp.languages"""

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from al_quran.comp.languages.models import Language
from al_quran.comp.languages.serializers import LanguageSerializer


# Create your views here.
class LanguageViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Translations"""

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "code"]
    ordering_fields = ["name", "code", "created_at", "updated_at"]
    filterset_fields = ["name", "code"]
