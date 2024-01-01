""" API endpoints for quran_api.chapters """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.permissions import IsReadOnly
from quran_api.chapters.models import Chapter
from quran_api.chapters.serializers import ChapterSerializer


# Create your views here.
class ChapterViewSet(ModelViewSet):
    """Create, view, update and delete"""

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated, IsReadOnly]
    search_fields = ["name"]
    ordering_fields = ["id", "name"]
    filterset_fields = ["name"]
