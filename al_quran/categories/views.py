""" API endpoints for al_quran.categories """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_quran.categories.models import Category
from al_quran.categories.serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(ReadOnlyModelViewSet):
    """List and retrieve Categories"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["id", "name"]
