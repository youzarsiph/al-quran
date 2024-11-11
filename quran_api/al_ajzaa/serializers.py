""" Serializers for quran_api.al_ajzaa """

from rest_framework.serializers import ModelSerializer
from quran_api.al_ajzaa.models import Juz


# Create your serializers here.
class JuzSerializer(ModelSerializer):
    """Part Serializer"""

    class Meta:
        """Meta data"""

        model = Juz
        fields = ["id", "url", "name", "verse_count", "created_at", "updated_at"]
