from django.db import models


class AlumniProfile(models.Model):
    name = models.CharField(max_length=120)
    graduation_year = models.PositiveIntegerField()
    current_role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    achievements = models.TextField(blank=True)

    def __str__(self):
        return self.name
