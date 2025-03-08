from django.db import models

from accounts.abstracts import UniversalIdModel, TimeStampedModel, ReferenceSlugModel
from chapters.models import Chapter


class Verse(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, related_name="verses"
    )
    verse_number = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Verse"
        verbose_name_plural = "Verses"
        ordering = ["number"]
        unique_together = ("chapter", "number")

    def __str__(self):
        return f"{self.chapter.book.name} {self.chapter.number}:{self.verse_number}"
