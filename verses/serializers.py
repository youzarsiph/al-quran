""" Serializers for quran_api.verses """


from rest_framework.serializers import HyperlinkedModelSerializer
from quran_api.verses.models import Verse


# Create your serializers here.
class VerseSerializer(HyperlinkedModelSerializer):
    """Verse Serializer"""

    class Meta:
        """Meta data"""

        model = Verse
        read_only_fields = []
        fields = ["id", "url"]
