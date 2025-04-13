"""Serializers for al_quran.comp.collections"""

from rest_framework.serializers import ModelSerializer

from al_quran.comp.collections.models import Collection


# Create your serializers here.
class CollectionSerializer(ModelSerializer):
    """Collection Serializer"""

    class Meta:
        """Meta data"""

        model = Collection
        fields = [
            "id",
            "url",
            "language",
            "type",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]
