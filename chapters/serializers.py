from rest_framework import serializers

from chapters.models import Chapter
from books.models import Book


class ChapterSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        queryset=Book.objects.all(), slug_field="reference"
    )

    class Meta:
        model = Chapter
        fields = (
            "book",
            "number",
            "name",
            "copyright",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
