""" Serializers for quran_api.i18n.translations """

from rest_framework.serializers import ModelSerializer

from quran_api.i18n.translations.models import Translation


# Create your serializers here.
class TranslationSerializer(ModelSerializer):
    """Translation Serializer"""

    class Meta:
        """Meta data"""

        model = Translation
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
