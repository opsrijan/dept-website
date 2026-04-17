from django.contrib import admin

from .models import AcademicProgram


@admin.register(AcademicProgram)
class AcademicProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "degree_type", "duration_years", "is_active")
    list_filter = ("degree_type", "is_active")
    search_fields = ("title",)
