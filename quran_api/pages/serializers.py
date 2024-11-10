""" Serializers for quran_api.pages """

from rest_framework.serializers import ModelSerializer
from quran_api.pages.models import Page
from quran_api.verses.serializers import PageVerseSerializer


# Create your serializers here.
class PageSerializer(ModelSerializer):
    """Page Serializer"""

    class Meta:
        """Meta data"""

        model = Page
        fields = [
            "id",
            "url",
            "chapter",
            "part",
            "group",
            "quarter",
            "verse_count",
            "created_at",
            "updated_at",
        ]


class ChapterPageSerializer(PageSerializer):
    """Pages serializer for chapters"""

    verses = PageVerseSerializer(many=True)

    class Meta(PageSerializer.Meta):
        """Meta data"""

        depth = 1
        fields = ["id", "url", "verse_count", "verses"]


class PageRetrieveSerializer(ChapterPageSerializer):
    """Page serializer for retrieve action"""

    class Meta(ChapterPageSerializer.Meta):
        """Meta data"""

        fields = PageSerializer.Meta.fields + ["verses"]
