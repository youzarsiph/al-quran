""" Serializers for quran_api.quarters """

from rest_framework.serializers import ModelSerializer
from quran_api.pages.serializers import ChapterPageSerializer
from quran_api.quarters.models import Quarter


# Create your serializers here.
class QuarterSerializer(ModelSerializer):
    """Quarter Serializer"""

    class Meta:
        """Meta data"""

        model = Quarter
        fields = ["id", "url", "verse_count", "created_at", "updated_at"]


class QuarterRetrieveSerializer(QuarterSerializer):
    """Quarter serializer for retrieve action"""

    pages = ChapterPageSerializer(many=True)

    class Meta(QuarterSerializer.Meta):
        """Meta data"""

        depth = 1
        fields = QuarterSerializer.Meta.fields + ["pages"]
