from django import forms
from .models import Post

__author__ = 'amanda'


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text'),

