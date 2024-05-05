""" Serializers for quran_api.chapters """

from rest_framework.serializers import ModelSerializer
from quran_api.chapters.models import Chapter


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
            "transliteration",
            "is_meccan",
            "verse_count",
            "created_at",
            "updated_at",
        ]
