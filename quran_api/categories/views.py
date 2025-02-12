""" API endpoints for quran_api.categories """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from quran_api.categories.models import Category
from quran_api.categories.serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(ReadOnlyModelViewSet):
    """List and retrieve Categories"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["id", "name"]
