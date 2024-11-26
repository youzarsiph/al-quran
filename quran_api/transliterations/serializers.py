""" Serializers for quran_api.transliterations """

from rest_framework.serializers import ModelSerializer

from quran_api.transliterations.models import Transliteration


# Create your serializers here.
class TransliterationSerializer(ModelSerializer):
    """Transliteration Serializer"""

    class Meta:
        """Meta data"""

        model = Transliteration
        fields = [
            "id",
            "url",
            "language",
            "chapter",
            "verse",
            "content",
            "created_at",
            "updated_at",
        ]
