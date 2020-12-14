from .models import DiaryPost


def list_diary_post(request):
    diarys = DiaryPost.objects.select_related('created_by').all()


def detail_diary_post(request):
    pass


def edit_diary_post(request):
    pass


def delete_diary_post(request):
    pass
