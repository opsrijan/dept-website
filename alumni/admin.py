from django.contrib import admin

from .models import AlumniProfile


@admin.register(AlumniProfile)
class AlumniProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "graduation_year", "current_role", "company")
    list_filter = ("graduation_year",)
    search_fields = ("name", "company")
