from django.db import models
from ckeditor.fields import RichTextField


class DiaryPost(models.Model):
    title = models.CharField(max_length=25)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
