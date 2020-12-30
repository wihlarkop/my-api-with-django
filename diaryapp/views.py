import json

from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import DiaryPost
from utils.response_data import JsonResponse
from utils.string_converter import convert_format_datetime_from_queryset
from utils.pagination import get_page_limit_offset_from_limit_page


async def list_diary_post(request):
    query = await DiaryPost.get_list_diary_posts()

    page, limit, offset = get_page_limit_offset_from_limit_page(request)

    query = query[offset:offset + limit]

    list_post = []

    for data in query:
        raw_data_created_at = str(data.created_at)
        created_at = convert_format_datetime_from_queryset(raw_data_created_at)

        list_post.append({
            'id': data.id,
            'title': data.title,
            'content': data.content,
            'created_at': created_at,
        })

    return JsonResponse(data=list_post,
                        code=200,
                        messages='Success Get Diary Data',
                        meta={
                            'page': page,
                            'limit': limit,
                            'offset': offset
                        })


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

    return JsonResponse(data=diary_data, messages='Success Add Diary', code=200)


def edit_diary_post(request, diaryid):
    pass


def delete_diary_post(request, diaryid):
    diary = get_object_or_404(DiaryPost, id=diaryid)

    if diary:
        diary.delete()

    return JsonResponse(data=None, messages='Success Delete Diary', code=200)
