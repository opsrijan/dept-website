from django.contrib import admin

from .models import PlacementRecord


@admin.register(PlacementRecord)
class PlacementRecordAdmin(admin.ModelAdmin):
    list_display = ("student_name", "company_name", "package_lpa", "year")
    list_filter = ("year",)
    search_fields = ("student_name", "company_name")
