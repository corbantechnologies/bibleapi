from django.db import models

from accounts.abstracts import UniversalIdModel, TimeStampedModel, ReferenceSlugModel
from verses.models import Verse


class VerseText(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE, related_name="texts")
    text = models.TextField()

    class Meta:
        verbose_name = "Verse Text"
        verbose_name_plural = "Verse Texts"
        unique_together = ("verse", "text")

    def __str__(self):
        return f"{self.verse.chapter.book.name} {self.verse.chapter.number}:{self.verse.verse_number}"
