from django.db import models

class GalleryImage(models.Model):
    title      = models.CharField(max_length=200)
    image_url  = models.URLField(max_length=500)
    year       = models.IntegerField()
    category   = models.CharField(max_length=100, default='General')

    class Meta:
        ordering = ['-year', 'id']

    def __str__(self):
        return f"{self.title} ({self.year})"