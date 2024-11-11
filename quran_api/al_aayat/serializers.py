""" Serializers for quran_api.al_aayat """

from rest_framework.serializers import ModelSerializer
from quran_api.al_aayat.models import Ayah


# Create your serializers here.
class AyahSerializer(ModelSerializer):
    """Ayah Serializer"""

    class Meta:
        """Meta data"""

        model = Ayah
        fields = [
            "id",
            "url",
            "sura",
            "juz",
            "hizb",
            "riba",
            "safhah",
            "number",
            "content",
        ]
