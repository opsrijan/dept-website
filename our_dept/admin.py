from django.contrib import admin
from django.utils.html import format_html
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display  = ('thumbnail', 'roll_number', 'name', 'batch', 'current_role', 'company')
    list_display_links = ('thumbnail', 'roll_number', 'name')
    list_filter   = ('batch',)
    search_fields = ('name', 'roll_number', 'company', 'current_role')
    ordering      = ('batch', 'roll_number')

    def thumbnail(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" style="width:44px;height:44px;'
                'object-fit:cover;border-radius:50%;" />',
                obj.profile_image.url,
            )
        return format_html(
            '<div style="width:44px;height:44px;border-radius:50%;'
            'background:#cbd5e1;display:flex;align-items:center;'
            'justify-content:center;font-size:20px;">👤</div>'
        )
    thumbnail.short_description = 'Photo'

from .models import PhDStudent

@admin.register(PhDStudent)
class PhDStudentAdmin(admin.ModelAdmin):
    list_display  = ('thumbnail', 'name', 'batch', 'interests')
    list_display_links = ('thumbnail', 'name')
    list_filter   = ('batch',)
    search_fields = ('name', 'interests', 'email')
    ordering      = ('batch', 'name')

    def thumbnail(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" style="width:44px;height:44px;'
                'object-fit:cover;border-radius:50%;" />',
                obj.profile_image.url,
            )
        return format_html(
            '<div style="width:44px;height:44px;border-radius:50%;'
            'background:#cbd5e1;display:flex;align-items:center;'
            'justify-content:center;font-size:20px;">👤</div>'
        )
    thumbnail.short_description = 'Photo'