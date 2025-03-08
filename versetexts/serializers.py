from rest_framework import serializers

from verses.models import Verse
from versetexts.models import VerseText


class VerseTextSerializer(serializers.ModelSerializer):
    verse = serializers.SlugRelatedField(
        queryset=Verse.objects.all(), slug_field="reference", write_only=True
    )
    verse_detail = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = VerseText
        fields = (
            "verse_name",
            "text",
            "reference",
            "slug",
            "verse",
            "verse_detail",
        )

    def get_verse_detail(self, obj):
        obj = obj.verse
        return {
            "chapter": obj.chapter.name,
            "verse_number": obj.verse_number,
            "reference": obj.reference,
            "slug": obj.slug,
        }
