from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
