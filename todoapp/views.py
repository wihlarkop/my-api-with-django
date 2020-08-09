from django.shortcuts import render


def add_todo(request):
    return render(request, 'todoapp/index.html')
