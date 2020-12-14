from ckeditor.widgets import CKEditorWidget

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.CharField(widget=CKEditorWidget)
        }