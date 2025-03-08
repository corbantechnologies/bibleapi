from django.db import models

from accounts.abstracts import UniversalIdModel, TimeStampedModel, ReferenceSlugModel
from chapters.models import Chapter


class Verse(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, related_name="verses"
    )
    verse_number = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Verse"
        verbose_name_plural = "Verses"
        ordering = ["chapter", "verse_number"]
        unique_together = ("chapter", "verse_number")

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = (
                f"{self.chapter.book.name} {self.chapter.number}:{self.verse_number}"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.chapter.book.name} {self.chapter.number}:{self.verse_number}"
