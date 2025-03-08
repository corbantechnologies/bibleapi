from rest_framework import serializers

from chapters.models import Chapter
from books.models import Book
from verses.serializers import VerseSerializer


class ChapterSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        queryset=Book.objects.all(), slug_field="reference", write_only=True
    )
    verses = VerseSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = (
            "book",
            "name",
            "number",
            "copyright",
            "created_at",
            "updated_at",
            "slug",
            "reference",
            "verses",
        )
