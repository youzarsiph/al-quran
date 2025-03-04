"""Serializers for al_quran.i18n.authors"""

from rest_framework.serializers import ModelSerializer

from al_quran.i18n.authors.models import Author


# Create your serializers here.
class AuthorSerializer(ModelSerializer):
    """Author Serializer"""

    class Meta:
        """Meta data"""

        model = Author
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
