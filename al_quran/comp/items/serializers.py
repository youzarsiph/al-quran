"""Serializers for al_quran.comp.items"""

from rest_framework.serializers import ModelSerializer

from al_quran.comp.items.models import Item


# Create your serializers here.
class ItemSerializer(ModelSerializer):
    """Item Serializer"""

    class Meta:
        """Meta data"""

        model = Item
        fields = [
            "id",
            "url",
            "collection",
            "chapter",
            "verse",
            "content",
            "created_at",
            "updated_at",
        ]
