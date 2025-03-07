from rest_framework import serializers

from books.models import Book
from translations.models import Translation


class BookSerializer(serializers.ModelSerializer):
    translation = serializers.SlugRelatedField(
        queryset=Translation.objects.all(), slug_field="name"
    )

    class Meta:
        model = Book
        fields = (
            "translation",
            "name",
            "abbreviation",
            "testament",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
