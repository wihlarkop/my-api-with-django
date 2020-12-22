from django.contrib import admin

from .models import DiaryPost


class DiaryPostAdmin(admin.ModelAdmin):
    model = DiaryPost
    list_display = ['id', 'title', 'created_at', 'created_by']


admin.site.register(DiaryPost, DiaryPostAdmin)
