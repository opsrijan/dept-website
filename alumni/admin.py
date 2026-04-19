from django.contrib import admin
from .models import Alumni


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display  = ('name', 'batch', 'company', 'role', 'email')
    list_filter   = ('batch',)
    search_fields = ('name', 'company', 'role')