"""Serializers for al_quran.quarters"""

from rest_framework.serializers import ModelSerializer

from al_quran.quarters.models import Quarter


# Create your serializers here.
class QuarterSerializer(ModelSerializer):
    """Quarter Serializer"""

    class Meta:
        """Meta data"""

        model = Quarter
        fields = [
            "id",
            "url",
            "group",
            "name",
            "verse_count",
            "page_count",
            "created_at",
            "updated_at",
        ]
