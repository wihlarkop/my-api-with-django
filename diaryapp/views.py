from django.shortcuts import render, redirect

from .models import DiaryPost
from .forms import DiaryPostForm


def list_diary_post(request):
    diarys = DiaryPost.objects.select_related('created_by').all()
    form = DiaryPostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('diaryapp:list_diary_post')
        else:
            form = DiaryPostForm()
    context = {
        'diarys': diarys,
        'form': form,
    }
    return render(request, 'diaryapp/index.html', context=context)


def detail_diary_post(request):
    pass


def edit_diary_post(request):
    pass


def delete_diary_post(request):
    pass
