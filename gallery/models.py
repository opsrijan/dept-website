from django.db import models


class GalleryItem(models.Model):
    title = models.CharField(max_length=150)
    image_url = models.URLField()
    event_name = models.CharField(max_length=150, blank=True)
    event_date = models.DateField(null=True, blank=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        return self.title
