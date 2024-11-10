""" Serializers for quran_api.parts """

from rest_framework.serializers import ModelSerializer
from quran_api.pages.serializers import ChapterPageSerializer
from quran_api.parts.models import Part


# Create your serializers here.
class PartSerializer(ModelSerializer):
    """Part Serializer"""

    class Meta:
        """Meta data"""

        model = Part
        fields = ["id", "url", "verse_count", "created_at", "updated_at"]


class PartRetrieveSerializer(PartSerializer):
    """Part serializer for retrieve action"""

    pages = ChapterPageSerializer(many=True)

    class Meta(PartSerializer.Meta):
        """Meta data"""

        depth = 1
        fields = PartSerializer.Meta.fields + ["pages"]
