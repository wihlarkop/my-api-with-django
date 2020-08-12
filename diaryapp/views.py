from django.shortcuts import render, redirect
from .models import DiaryPost
from .forms import DiaryPostForm


def list_diary_post(request):
    diarys = DiaryPost.objects.all()
    form = DiaryPostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('diaryapp:list_diary_post')
        else:
            form = DiaryPostForm()
    context = {
        'list': diarys,
        'form': form,
    }

    return render(request, 'diaryapp/list_diary_post.html', context=context)


def add_diary_post(request):
    pass


def edit_diary_post(request):
    pass


def delete_diary_post(request):
    pass
