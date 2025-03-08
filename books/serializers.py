from rest_framework import serializers

from books.models import Book
from translations.models import Translation
from chapters.serializers import ChapterSerializer


class BookSerializer(serializers.ModelSerializer):
    translation = serializers.SlugRelatedField(
        queryset=Translation.objects.all(), slug_field="name", write_only=True
    )
    chapters = ChapterSerializer(many=True, read_only=True)

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
            "chapters",
        )
