from django.contrib import admin

from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "email", "joined_on")
    list_filter = ("designation",)
    search_fields = ("name", "designation")
