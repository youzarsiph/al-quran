""" Serializers for quran_api.al_ahzab """

from rest_framework.serializers import ModelSerializer
from quran_api.al_ahzab.models import Hizb


# Create your serializers here.
class HizbSerializer(ModelSerializer):
    """Hizb Serializer"""

    class Meta:
        """Meta data"""

        model = Hizb
        fields = ["id", "url", "name", "verse_count", "created_at", "updated_at"]
