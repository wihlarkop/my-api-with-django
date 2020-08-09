from django.shortcuts import render


def list_diary_post(request):
    return render(request, 'diaryapp/list_diary_post.html')
