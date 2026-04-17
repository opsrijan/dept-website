from django.contrib import admin

from .models import InternshipOpportunity


@admin.register(InternshipOpportunity)
class InternshipOpportunityAdmin(admin.ModelAdmin):
    list_display = ("company_name", "role", "stipend", "deadline")
    list_filter = ("deadline",)
    search_fields = ("company_name", "role")
