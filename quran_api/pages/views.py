""" API endpoints for quran_api.pages """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from quran_api.pages.models import Page
from quran_api.pages.serializers import PageRetrieveSerializer, PageSerializer


# Create your views here.
class PageViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran Pages with filtering and sorting support"""

    queryset = Page.objects.select_related("chapter", "part", "group", "quarter")
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id"]
    filterset_fields = ["id", "chapter", "part", "group", "quarter"]

    def get_serializer_class(self):
        """Customize serializer_class based on self.action"""

        if self.action == "retrieve":
            self.serializer_class = PageRetrieveSerializer

        return super().get_serializer_class()
