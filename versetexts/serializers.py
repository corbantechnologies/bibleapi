from rest_framework import serializers

from verses.models import Verse
from versetexts.models import VerseText


class VerseTextSerializer(serializers.ModelSerializer):
    verse = serializers.SlugRelatedField(
        queryset=Verse.objects.all(), slug_field="reference", write_only=True
    )

    class Meta:
        model = VerseText
        fields = (
            "verse_name",
            "text",
            "reference",
            "slug",
            "verse",
        )
