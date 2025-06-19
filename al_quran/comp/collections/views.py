"""API endpoints for al_quran.comp.collections"""

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from al_quran.comp.collections.models import Collection
from al_quran.comp.collections.serializers import CollectionSerializer


# Create your views here.
class CollectionViewSet(ReadOnlyModelViewSet):
    """List and retrieve Collections"""

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["language", "type"]
