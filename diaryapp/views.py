from datetime import datetime

from asgiref.sync import sync_to_async

from utils.response_data import JsonReseponse
from utils.string_converter import convert_string_data_to_datetime
from .models import DiaryPost


@sync_to_async
def list_diary_post(request):
    query = DiaryPost.objects.all()

    list_post = []

    for data in query:
        raw_data_created_at = str(data.created_at)
        created_at = convert_string_data_to_datetime(raw_data_created_at)

        list_post.append({
            'title': data.title,
            'content': data.content,
            'created_at': created_at,
            'author': data.created_by.username
        })

    return JsonReseponse(list_post, code=200, messages='Success Get Diary Data')


def create_diary_post(request):
    pass


def edit_diary_post(request):
    pass


def delete_diary_post(request):
    pass
