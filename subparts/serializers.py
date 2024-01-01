""" Serializers for quran_api.subparts """


from rest_framework.serializers import HyperlinkedModelSerializer
from quran_api.subparts.models import Subpart


# Create your serializers here.
class SubpartSerializer(HyperlinkedModelSerializer):
    """Subpart Serializer"""

    class Meta:
        """Meta data"""

        model = Subpart
        fields = ["id", "url"]
