""" Serializers for quran_api.as_suwar """

from rest_framework.serializers import ModelSerializer
from quran_api.as_suwar.models import Sura


# Create your serializers here.
class SuraSerializer(ModelSerializer):
    """Sura Serializer"""

    class Meta:
        """Meta data"""

        model = Sura
        fields = [
            "id",
            "url",
            "name",
            "order",
            "type",
            "verse_count",
            "created_at",
            "updated_at",
        ]
