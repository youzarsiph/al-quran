""" Serializers for al_quran.pages """

from rest_framework.serializers import ModelSerializer

from al_quran.pages.models import Page


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
            "quarter",
            "name",
            "verse_count",
            "created_at",
            "updated_at",
        ]
