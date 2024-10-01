from django.forms import ModelForm
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms

class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].required = False

    class Meta:
        model = Post
        fields = ['title', 'category', 'text']
