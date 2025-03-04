"""Serializers for al_quran.i18n.categories"""

from rest_framework.serializers import ModelSerializer

from al_quran.i18n.categories.models import Category


# Create your serializers here.
class CategorySerializer(ModelSerializer):
    """Category Serializer"""

    class Meta:
        """Meta data"""

        model = Category
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
