from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=120)
    designation = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    profile_link = models.URLField(blank=True)
    joined_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.designation})"
