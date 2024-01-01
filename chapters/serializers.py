""" Serializers for quran_api.chapters """


from rest_framework.serializers import HyperlinkedModelSerializer
from quran_api.chapters.models import Chapter


# Create your serializers here.
class ChapterSerializer(HyperlinkedModelSerializer):
    """Chapter Serializer"""

    class Meta:
        """Meta data"""

        model = Chapter
        fields = ["id", "url"]
