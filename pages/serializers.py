""" Serializers for quran_api.pages """


from rest_framework.serializers import HyperlinkedModelSerializer
from quran_api.pages.models import Page


# Create your serializers here.
class PageSerializer(HyperlinkedModelSerializer):
    """Page Serializer"""

    class Meta:
        """Meta data"""

        model = Page
        fields = ["id", "url"]
