from django import forms
from .models import DiaryPost
from ckeditor.widgets import CKEditorWidget


class DiaryPostForm(forms.ModelForm):
    class Meta:
        model = DiaryPost
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control'}))
        }
