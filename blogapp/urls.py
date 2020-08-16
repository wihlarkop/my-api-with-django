from django.urls import path

from .views import add_post, delete_post, detail_post, edit_post, list_post

app_name = 'blogapp'

urlpatterns = [
    path('list/', list_post, name='list_post'),
    path('add/', add_post, name='add_post'),
    path('edit/', edit_post, name='edit_post'),
    path('delete/', delete_post, name='delete_post'),
    path('detail/', detail_post, name='detail_post'),
]
