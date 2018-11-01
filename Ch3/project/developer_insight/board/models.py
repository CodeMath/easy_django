from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    STATUS = {
        ('normal', "status_normal"),
        ('deleted', 'status_deleted')
    }
    table = models.IntegerField(verbose_name="테이블 id")
    title = models.CharField(verbose_name="제목", max_length=50)
    status = models.CharField(max_length=20, verbose_name="상태", choices=STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(verbose_name="내용")

    up_vote = models.IntegerField(verbose_name="추천", default=0)
    down_vote = models.IntegerField(verbose_name="비추천", default=0)

    up_vote_user = models.ManyToManyField(User, related_name="up_vote_user")
    down_vote_user = models.ManyToManyField(User, related_name="down_vote_user")
    ip = models.GenericIPAddressField(default="127.0.0.1")

    def __str__(self):
        return "[%s] %s" %(self.user.username, self.title )


class Reply(models.Model):
    article_id = models.IntegerField(verbose_name="게시글 번호")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    created_at = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(default="127.0.0.1")
    content = models.TextField(max_length=2000,verbose_name="내용")

    def __str__(self):
        return "[%s]" %(self.user.username)