""" Serializers for quran_api.parts """


from rest_framework.serializers import HyperlinkedModelSerializer
from quran_api.parts.models import Part


# Create your serializers here.
class PartSerializer(HyperlinkedModelSerializer):
    """Part Serializer"""

    class Meta:
        """Meta data"""

        model = Part
        fields = ["id", "url"]
