""" API endpoints for al_quran.authors """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_quran.authors.models import Author
from al_quran.authors.serializers import AuthorSerializer


# Create your views here.
class AuthorViewSet(ReadOnlyModelViewSet):
    """List and retrieve Authors"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["id", "name"]
