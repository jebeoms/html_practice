from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body', 'imgfile']
        labels={
            'imgfile': '첨부파일',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']

