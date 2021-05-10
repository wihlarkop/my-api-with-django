import json

from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from diaryapi.models import DiaryPost
from diaryapi.schema import DiaryPostSchema
from utils.custom_response import JsonResponse
from utils.date_convert import date_convert


@csrf_exempt
def diary_add(request):
    body = json.loads(request.body)
    title = body.get('title', None)
    content = body.get('content', None)

    schema = DiaryPostSchema(title=title, content=content)

    diary_data = {
        'title': schema.title,
        'content': schema.content,
    }

    diary = DiaryPost.objects.create(**diary_data)
    diary.save()

    return JsonResponse(data=None, messages='Success Add Diary', code=200)


async def diary_list(request):
    query = await DiaryPost.get_list_diary_posts()

    list_post = []

    for data in query:
        list_post.append({
            'id': data.id,
            'title': data.title,
            'content': data.content,
            'created_at': date_convert(data.created_at),
        })

    return JsonResponse(data=list_post, code=200, messages='Success Get Diary Data')

# def edit_diary_post(request, diaryid):
#     pass
#
#
# def delete_diary_post(request, diaryid):
#     diary = get_object_or_404(DiaryPost, id=diaryid)
#
#     if diary:
#         diary.delete()
#
#     return JsonResponse(data=None, messages='Success Delete Diary', code=200)
