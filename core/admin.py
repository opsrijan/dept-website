from django.contrib import admin

from .models import DepartmentInfo


@admin.register(DepartmentInfo)
class DepartmentInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "established_year", "updated_at")
    search_fields = ("name",)
