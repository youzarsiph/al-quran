""" Serializers for quran_api.groups """

from rest_framework.serializers import ModelSerializer
from quran_api.groups.models import Group
from quran_api.pages.serializers import ChapterPageSerializer


# Create your serializers here.
class GroupSerializer(ModelSerializer):
    """Group Serializer"""

    class Meta:
        """Meta data"""

        model = Group
        fields = ["id", "url", "verse_count", "created_at", "updated_at"]


class GroupRetrieveSerializer(GroupSerializer):
    """Group serializer for retrieve action"""

    pages = ChapterPageSerializer(many=True)

    class Meta(GroupSerializer.Meta):
        """Meta data"""

        depth = 1
        fields = GroupSerializer.Meta.fields + ["pages"]
