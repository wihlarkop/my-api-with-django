from asgiref.sync import sync_to_async
from django.db import models


class DiaryPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    @staticmethod
    def get_list_diary_posts():
        return sync_to_async(list)(DiaryPost.objects.all())
