from django.urls import path
from .views import list_diary_post

app_name = 'diaryapp'

urlpatterns = [
    path('list/', list_diary_post, name='list_diary_post'),
]
