from rest_framework import serializers

from chapters.models import Chapter
from verses.models import Verse


class VerseSerializer(serializers.ModelSerializer):
    chapter = serializers.SlugRelatedField(
        queryset=Chapter.objects.all(), slug_field="reference"
    )
    chapter_detail = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Verse
        fields = (
            "chapter",
            "verse_number",
            "reference",
            "slug",
            "chapter_detail",
        )

    def get_chapter_detail(self, obj):
        obj = obj.chapter
        return {
            "name": obj.name,
            "number": obj.number,
            "reference": obj.reference,
            "slug": obj.slug,
        }
