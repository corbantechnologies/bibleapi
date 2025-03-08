from rest_framework import serializers

from verses.models import Verse
from versetexts.models import VerseText


class VerseTextSerializer(serializers.ModelSerializer):
    verse = serializers.SlugRelatedField(
        queryset=Verse.objects.all(), slug_field="reference"
    )

    class Meta:
        model = VerseText
        fields = (
            "verse",
            "text",
            "reference",
            "slug",
        )
