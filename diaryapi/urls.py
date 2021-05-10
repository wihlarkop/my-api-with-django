from django.urls import path
from .views import (diary_list, diary_add)

app_name = 'diaryapi'

urlpatterns = [
    path('list', diary_list, name='diary_list'),
    path('add', diary_add, name='diary_add'),
    # path('edit/<int:diaryid>', edit_diary_post, name='list_diary_post'),
    # path('delete/<int:diaryid>', delete_diary_post, name='list_diary_post'),
]
