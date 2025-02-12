""" API endpoints for quran_api.books """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from quran_api.books.models import Book
from quran_api.books.serializers import BookSerializer


# Create your views here.
class BookViewSet(ReadOnlyModelViewSet):
    """List and retrieve Books"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["id", "name"]
