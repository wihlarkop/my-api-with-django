from django.contrib import admin

from .models import DiaryPost


@admin.register(DiaryPost)
class DiaryPostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'created_at',
        'modified_at'
    )
    ordering = 'created_at'
