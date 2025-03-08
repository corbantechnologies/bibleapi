from django.db import models

from accounts.abstracts import UniversalIdModel, TimeStampedModel, ReferenceSlugModel
from verses.models import Verse


class VerseText(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE, related_name="texts")
    text = models.TextField()
    verse_name = models.CharField(blank=True, max_length=255)

    class Meta:
        verbose_name = "Verse Text"
        verbose_name_plural = "Verse Texts"
        unique_together = ("verse", "text")

    def save(self, *args, **kwargs):
        if not self.verse_name:
            # Genesis 1:1
            self.verse_name = f"{self.verse.chapter.name}:{self.verse.verse_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.verse.chapter.book.name} {self.verse.chapter.number}:{self.verse.verse_number}"
