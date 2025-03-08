from django.db import models

from accounts.abstracts import UniversalIdModel, TimeStampedModel, ReferenceSlugModel
from translations.models import Translation


class Book(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    translation = models.ForeignKey(
        Translation, on_delete=models.CASCADE, related_name="books"
    )
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=25)
    testament = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["created_at"]
        unique_together = ("translation", "name")

    def __str__(self):
        return f"{self.name} - {self.translation.abbreviation}"
