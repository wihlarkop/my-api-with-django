from django.urls import path
from .views import (list_diary_post, create_diary_post, delete_diary_post, edit_diary_post)

app_name = 'diaryapp'

urlpatterns = [
    path('list/', list_diary_post, name='list_diary_post'),
    path('create/', create_diary_post, name='list_diary_post'),
    path('edit/<int:diaryid>', edit_diary_post, name='list_diary_post'),
    path('delete/<int:diaryid>', delete_diary_post, name='list_diary_post'),
]
