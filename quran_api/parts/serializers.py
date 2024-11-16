""" Serializers for quran_api.parts """

from rest_framework.serializers import ModelSerializer

from quran_api.parts.models import Part


# Create your serializers here.
class PartSerializer(ModelSerializer):
    """Part Serializer"""

    class Meta:
        """Meta data"""

        model = Part
        fields = [
            "id",
            "url",
            "name",
            "verse_count",
            "page_count",
            "created_at",
            "updated_at",
        ]
