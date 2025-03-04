"""Serializers for al_quran.core.verses"""

from rest_framework.serializers import ModelSerializer

from al_quran.core.verses.models import Verse


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
            "content",
        ]
