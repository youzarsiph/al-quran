""" API endpoints for quran_api.authors """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from quran_api.authors.models import Author
from quran_api.authors.serializers import AuthorSerializer


# Create your views here.
class AuthorViewSet(ReadOnlyModelViewSet):
    """List and retrieve Authors"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["id", "name"]
