""" Serializers for quran_api.as_safahat """

from rest_framework.serializers import ModelSerializer
from quran_api.as_safahat.models import Safhah


# Create your serializers here.
class SafhahSerializer(ModelSerializer):
    """Page Serializer"""

    class Meta:
        """Meta data"""

        model = Safhah
        fields = [
            "id",
            "url",
            "sura",
            "juz",
            "hizb",
            "riba",
            "verse_count",
            "created_at",
            "updated_at",
        ]
