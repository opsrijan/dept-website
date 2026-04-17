from django.contrib import admin

from .models import Opportunity


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ("title", "organizer", "opportunity_type", "apply_by")
    list_filter = ("opportunity_type",)
    search_fields = ("title", "organizer")
