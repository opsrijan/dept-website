from django.db import models


class InternshipOpportunity(models.Model):
    company_name = models.CharField(max_length=150)
    role = models.CharField(max_length=120)
    stipend = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.company_name} - {self.role}"
