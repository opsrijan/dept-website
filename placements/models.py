from django.db import models


class PlacementRecord(models.Model):
    student_name = models.CharField(max_length=120)
    company_name = models.CharField(max_length=150)
    package_lpa = models.DecimalField(max_digits=6, decimal_places=2)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.company_name}"
