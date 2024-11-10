""" Serializers for quran_api.chapters """

from rest_framework.serializers import ModelSerializer
from quran_api.chapters.models import Chapter
from quran_api.pages.serializers import ChapterPageSerializer


# Create your serializers here.
class ChapterSerializer(ModelSerializer):
    """Chapter Serializer"""

    class Meta:
        """Meta data"""

        model = Chapter
        fields = [
            "id",
            "url",
            "name",
            "order",
            "type",
            "verse_count",
            "created_at",
            "updated_at",
        ]


class ChapterRetrieveSerializer(ChapterSerializer):
    """Chapter serializer for retrieve action"""

    pages = ChapterPageSerializer(many=True)

    class Meta(ChapterSerializer.Meta):
        """Meta data"""

        depth = 1
        fields = ChapterSerializer.Meta.fields + ["pages"]
