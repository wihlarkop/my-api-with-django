import json

from django.views.decorators.csrf import csrf_exempt

from .models import DiaryPost
from utils.response_data import JsonResponse
from utils.string_converter import convert_format_datetime_from_queryset


async def list_diary_post(request):
    query = await DiaryPost.get_list_diary_posts()
    list_post = []

    for data in query:
        raw_data_created_at = str(data.created_at)
        created_at = convert_format_datetime_from_queryset(raw_data_created_at)

        list_post.append({
            'title': data.title,
            'content': data.content,
            'created_at': created_at,
        })

    return JsonResponse(list_post, code=200, messages='Success Get Diary Data')


@csrf_exempt
def add_diary_post(request):
    body = json.loads(request.body)
    title = body.get('title', None)
    content = body.get('content', None)

    if title == '' or None:
        raise KeyError('Title is required')
    if content == '' or None:
        raise KeyError('Content is required')

    diary_data = {
        'title': title,
        'content': content,
    }

    diary = DiaryPost(**diary_data)
    diary.save()

    return JsonResponse(data=diary_data, messages='Success Add Diary')


def edit_diary_post(request):
    pass


def delete_diary_post(request):
    pass
