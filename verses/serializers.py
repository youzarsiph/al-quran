""" Serializers for quran_api.verses """

from rest_framework.serializers import ModelSerializer
from quran_api.verses.models import Verse


# Create your serializers here.
class VerseSerializer(ModelSerializer):
    """Verse Serializer"""

    class Meta:
        """Meta data"""

        model = Verse
        fields = [
            "id",
            "url",
            "chapter",
            "part",
            "group",
            "quarter",
            "page",
            "number",
            "text",
            "transliteration",
        ]


class PageVerseSerializer(VerseSerializer):
    """Verse serializer for pages"""

    class Meta(VerseSerializer.Meta):
        """Meta data"""

        fields = ["id", "url", "number", "text", "transliteration"]
