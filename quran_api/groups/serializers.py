""" Serializers for quran_api.groups """

from rest_framework.serializers import ModelSerializer

from quran_api.groups.models import Group


# Create your serializers here.
class GroupSerializer(ModelSerializer):
    """Group Serializer"""

    class Meta:
        """Meta data"""

        model = Group
        fields = [
            "id",
            "url",
            "part",
            "name",
            "verse_count",
            "page_count",
            "created_at",
            "updated_at",
        ]
