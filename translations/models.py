from django.db import models

from accounts.abstracts import UniversalIdModel, TimeStampedModel, ReferenceSlugModel


class Translation(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Translation"
        verbose_name_plural = "Translations"
        ordering = ["name"]

    def __str__(self):
        return self.name
