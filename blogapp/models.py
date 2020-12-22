from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    poster = models.ImageField(upload_to='post/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
