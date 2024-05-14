""" Serializers for quran_api.verses """

from rest_framework.serializers import ModelSerializer
from quran_api.verses.models import Verse


# Create your serializers here.
class VerseSerializer(ModelSerializer):
    """Verse Serializer"""

    class Meta:
        """Meta data"""

        model = Verse
        read_only_fields = ["chapter", "part", "group", "page"]
        fields = [
            "id",
            "url",
            "chapter",
            "part",
            "group",
            "page",
            "number",
            "text",
            "transliteration",
        ]
