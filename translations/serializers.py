from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from translations.models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Translation.objects.all())]
    )
    abbreviation = serializers.CharField(
        validators=[UniqueValidator(queryset=Translation.objects.all())]
    )

    class Meta:
        model = Translation
        fields = (
            "name",
            "abbreviation",
            "description",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
