from django.db import models

from accounts.abstracts import UniversalIdModel, TimeStampedModel, ReferenceSlugModel
from books.models import Book


class Chapter(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="chapters")
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True)
    copyright = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"
        ordering = ["number"]
        unique_together = ("book", "number")

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.book.name} {self.number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
