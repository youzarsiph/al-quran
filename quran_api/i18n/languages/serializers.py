""" Serializers for quran_api.i18n.languages """

from rest_framework.serializers import ModelSerializer

from quran_api.i18n.languages.models import Language


# Create your serializers here.
class LanguageSerializer(ModelSerializer):
    """Language Serializer"""

    class Meta:
        """Meta data"""

        model = Language
        fields = ["id", "url", "name", "code", "created_at", "updated_at"]
