""" Serializers for al_quran.books """

from rest_framework.serializers import ModelSerializer

from al_quran.books.models import Book


# Create your serializers here.
class BookSerializer(ModelSerializer):
    """Book Serializer"""

    class Meta:
        """Meta data"""

        model = Book
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
