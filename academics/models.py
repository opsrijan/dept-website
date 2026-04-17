from django.db import models


class AcademicProgram(models.Model):
    title = models.CharField(max_length=150)
    degree_type = models.CharField(max_length=80)
    duration_years = models.PositiveIntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
