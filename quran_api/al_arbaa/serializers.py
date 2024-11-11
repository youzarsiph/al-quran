""" Serializers for quran_api.al_arbaa """

from rest_framework.serializers import ModelSerializer
from quran_api.al_arbaa.models import Riba


# Create your serializers here.
class RibaSerializer(ModelSerializer):
    """Quarter Serializer"""

    class Meta:
        """Meta data"""

        model = Riba
        fields = ["id", "url", "name", "verse_count", "created_at", "updated_at"]
