"""Serializers for al_quran.i18n.items"""

from rest_framework.serializers import ModelSerializer

from al_quran.i18n.items.models import Item


# Create your serializers here.
class ItemSerializer(ModelSerializer):
    """Item Serializer"""

    class Meta:
        """Meta data"""

        model = Item
        fields = [
            "id",
            "url",
            "book",
            "chapter",
            "verse",
            "content",
            "created_at",
            "updated_at",
        ]
