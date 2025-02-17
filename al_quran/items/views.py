""" API endpoints for al_quran.items """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_quran.items.models import Item
from al_quran.items.serializers import ItemSerializer


# Create your views here.
class ItemViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Items like trans and interpretations"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["content"]
    ordering_fields = ["chapter", "verse", "created_at", "updated_at"]
    filterset_fields = [
        "book",
        "book__author",
        "book__category",
        "book__language",
        "chapter",
        "verse",
    ]
