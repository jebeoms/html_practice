from django.db import models
# from django.contrib.auth.models import User
from bcuser.models import Bcuser
from django.utils import timezone

class Post(models.Model):
    title=models.CharField(max_length=200, verbose_name='제목')
    body=models.TextField(verbose_name='본문')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    author=models.ForeignKey(Bcuser, on_delete=models.CASCADE, verbose_name='작성자')
    imgfile=models.ImageField(null=True, upload_to="", blank=True)  #이미지 칼럼 추가

    def __str__(self):
        return self.title
    
    class Meta:
        db_table='Post_table'
        verbose_name='포스트'
        verbose_name_plural='포스트들'


class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name='포스트')
    name=models.CharField(max_length=80, verbose_name='이름')
    body=models.TextField(verbose_name='본문')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    def __str__(self):
        return f'{self.name}-{self.post.title}'
    
    class Meta:
        db_table='Comment_table'
        verbose_name='댓글'
        verbose_name_plural='댓글들'