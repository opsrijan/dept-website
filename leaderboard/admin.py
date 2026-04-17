from django.contrib import admin

from .models import LeaderboardEntry


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ("rank", "name", "category", "score", "achieved_on")
    list_filter = ("category",)
    search_fields = ("name", "category")
