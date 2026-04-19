from django.db import models


class Alumni(models.Model):
    name       = models.CharField(max_length=200)
    batch      = models.IntegerField()
    email      = models.CharField(max_length=200, blank=True)
    phone      = models.CharField(max_length=50, blank=True)
    github     = models.URLField(max_length=300, blank=True)
    linkedin   = models.URLField(max_length=300, blank=True)
    company    = models.CharField(max_length=200, blank=True)
    role       = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-batch', 'name']

    def __str__(self):
        return f"{self.name} (Batch {self.batch})"