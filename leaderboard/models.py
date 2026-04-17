from django.db import models


class LeaderboardEntry(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=100)
    score = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()
    achieved_on = models.DateField()

    class Meta:
        ordering = ["rank"]

    def __str__(self):
        return f"#{self.rank} {self.name}"
