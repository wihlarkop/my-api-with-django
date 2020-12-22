from django.contrib.auth.models import User
from django.db import models


class DiaryPost(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='diary/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title
