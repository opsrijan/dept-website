from django.db import models

class Student(models.Model):
    BATCH_CHOICES = [
        ('2022-2026', '2022–2026'),
        ('2023-2027', '2023–2027'),
        ('2024-2028', '2024–2028'),
        ('2025-2029', '2025–2029'),
    ]

    name          = models.CharField(max_length=150)
    roll_number   = models.CharField(max_length=20)
    batch         = models.CharField(max_length=20, choices=BATCH_CHOICES)
    linkedin_url  = models.URLField(blank=True, null=True)
    email         = models.EmailField(blank=True, null=True)
    phone         = models.CharField(max_length=20, blank=True, null=True)
    github        = models.URLField(blank=True, null=True)
    current_role  = models.CharField(max_length=150, blank=True, null=True)
    company       = models.CharField(max_length=150, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to='students/profiles/',
        blank=True,
        null=True,
    )

    class Meta:
        ordering        = ['batch', 'roll_number']
        verbose_name        = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.roll_number} — {self.name} ({self.batch})"


class PhDStudent(models.Model):
    BATCH_CHOICES = [
        ('Dec 2021', 'Dec 2021'),
        ('Jul 2022', 'Jul 2022'),
        ('Dec 2022', 'Dec 2022'),
        ('Jul 2023', 'Jul 2023'),
        ('Dec 2023', 'Dec 2023'),
        ('Jul 2024', 'Jul 2024'),
        ('Dec 2024', 'Dec 2024'),
        ('Jul 2025', 'Jul 2025'),
    ]

    name          = models.CharField(max_length=150)
    batch         = models.CharField(max_length=20, choices=BATCH_CHOICES)
    interests     = models.CharField(max_length=255, blank=True, null=True)
    email         = models.EmailField(blank=True, null=True)
    phone         = models.CharField(max_length=20, blank=True, null=True)
    github        = models.URLField(blank=True, null=True)
    linkedin      = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to='phd/profiles/',
        blank=True,
        null=True,
    )

    class Meta:
        ordering            = ['batch', 'name']
        verbose_name        = 'PhD Student'
        verbose_name_plural = 'PhD Students'

    def __str__(self):
        return f"{self.name} ({self.batch})"