from django.db import models


class DepartmentInfo(models.Model):
    name = models.CharField(max_length=150)
    vision = models.TextField()
    mission = models.TextField()
    established_year = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Department Info"
        verbose_name_plural = "Department Info"

    def __str__(self):
        return self.name
