""" API endpoints for quran_api.pages """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.permissions import IsReadOnly
from quran_api.pages.models import Page
from quran_api.pages.serializers import PageSerializer


# Create your views here.
class PageViewSet(ModelViewSet):
    """Create, view, update and delete"""

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated, IsReadOnly]
    search_fields = []
    ordering_fields = [
        "id",
    ]
    filterset_fields = []
