"""API endpoints for al_quran.core.verses"""

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from al_quran.core.verses.models import Verse
from al_quran.core.verses.serializers import VerseSerializer


# Create your views here.
class VerseViewSet(ReadOnlyModelViewSet):
    """List and retrieve Quran verses"""

    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["content"]
    ordering_fields = ["number", "created_at", "updated_at"]
    filterset_fields = ["id", "chapter", "part", "group", "quarter", "page", "number"]

    @action(methods=["post"], detail=True)
    def bookmark(self, request: Request, pk: int) -> Response:
        """Un/Bookmark a verse

        Args:
            request (Request): HTTP Request

        Returns:
            Response: HTTPResponse
        """

        message: str
        verse = self.get_object()

        if request.user.bookmarks.contains(verse):
            request.user.bookmarks.remove(verse)
            message = _("Bookmark removed")

        else:
            message = _("Bookmark added")
            request.user.bookmarks.add(verse)

        if request.query_params["redirect"]:
            messages.success(request, message)
            return redirect(
                reverse_lazy("al-quran:chapter", args=[verse.chapter_id])
                + f"#verse-{verse.chapter_id}:{verse.number}"
            )

        return Response({"details": message}, status=status.HTTP_200_OK)
