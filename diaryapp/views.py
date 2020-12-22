from utils.response_data import JsonReseponse
from .models import DiaryPost


def list_diary_post(request):
    query = DiaryPost.objects.all()

    list_post = []

    for data in query:
        list_post.append({
            'title': data.title,
            'content': data.content,
            'created_at': data.created_at,
            'author': data.created_by.username
        })

    return JsonReseponse(list_post, code=200)


def create_diary_post(request):
    pass


def edit_diary_post(request):
    pass


def delete_diary_post(request):
    pass
