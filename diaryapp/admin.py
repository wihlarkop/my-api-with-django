from django.contrib import admin
from .models import DiaryPost


class DiaryPostAdmin(admin.ModelAdmin):
    model = DiaryPost
    list_display = ['id', 'title']


admin.site.register(DiaryPost, DiaryPostAdmin)
