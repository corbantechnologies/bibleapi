from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from translations.models import Translation
from books.serializers import BookSerializer


class TranslationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Translation.objects.all())]
    )
    abbreviation = serializers.CharField(
        validators=[UniqueValidator(queryset=Translation.objects.all())]
    )
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Translation
        fields = (
            "name",
            "abbreviation",
            "created_at",
            "updated_at",
            "slug",
            "reference",
            "books",
        )
