from rest_framework import serializers

from chapters.models import Chapter
from verses.models import Verse


class VerseSerializer(serializers.ModelSerializer):
    chapter = serializers.SlugRelatedField(
        queryset=Chapter.objects.all(), slug_field="reference"
    )

    class Meta:
        model = Verse
        fields = (
            "chapter",
            "verse_number",
            "reference",
            "slug",
        )
