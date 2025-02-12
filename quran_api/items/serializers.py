""" Serializers for quran_api.items """

from rest_framework.serializers import ModelSerializer

from quran_api.items.models import Item


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
