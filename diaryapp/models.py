from asgiref.sync import sync_to_async
from django.db import models


class DiaryPost(models.Model):
    title = models.CharField(max_length=125)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='diary/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_list_diary_posts():
        return sync_to_async(list)(DiaryPost.objects.all())
