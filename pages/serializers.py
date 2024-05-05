""" Serializers for quran_api.pages """

from rest_framework.serializers import ModelSerializer
from quran_api.pages.models import Page


# Create your serializers here.
class PageSerializer(ModelSerializer):
    """Page Serializer"""

    class Meta:
        """Meta data"""

        model = Page
        fields = [
            "id",
            "url",
            "chapter",
            "part",
            "group",
            "verse_count",
            "created_at",
            "updated_at",
        ]
