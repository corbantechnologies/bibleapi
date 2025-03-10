from rest_framework import serializers

from chapters.models import Chapter
from verses.models import Verse
from versetexts.serializers import VerseTextSerializer


class VerseSerializer(serializers.ModelSerializer):
    chapter = serializers.SlugRelatedField(
        queryset=Chapter.objects.all(), slug_field="reference", write_only=True
    )
    texts = VerseTextSerializer(many=True, read_only=True)

    class Meta:
        model = Verse
        fields = (
            "chapter",
            "name",
            "verse_number",
            "reference",
            "slug",
            "created_at",
            "updated_at",
            "texts",
        )
