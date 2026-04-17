from django.db import models


class Opportunity(models.Model):
    title = models.CharField(max_length=180)
    organizer = models.CharField(max_length=150)
    opportunity_type = models.CharField(max_length=80)
    apply_by = models.DateField()
    details = models.TextField()

    def __str__(self):
        return self.title
