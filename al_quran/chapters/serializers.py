""" Serializers for al_quran.chapters """

from rest_framework.serializers import ModelSerializer

from al_quran.chapters.models import Chapter


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
            "page_count",
            "created_at",
            "updated_at",
        ]
