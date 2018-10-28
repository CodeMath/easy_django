# fund/models.py
from django.db import models
from django.contrib.auth.models import User  # (1) django models 중 User(사용자)
from django.core.validators import MaxValueValidator, MinValueValidator


class Reward(models.Model):  # (2)펀딩에 연결될 리워드
    subject = models.CharField(max_length=200, verbose_name="리워드 제목")
    content = models.TextField(verbose_name="내용")
    # price = models.PositiveIntegerField(default=1000, verbose_name="금액")
    price = models.PositiveIntegerField(default=1000, verbose_name="금액", validators = [MinValueValidator(1000), MaxValueValidator(10000000)])
    number = models.IntegerField(default=0, verbose_name="수량")

    def __str__(self):
        return self.subject


class Funding(models.Model):  # (3) 펀딩 리스트
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="게시자")
    title = models.CharField(max_length=250, verbose_name="펀딩 제목")
    content = models.TextField(verbose_name="내용")
    main_img = models.ImageField(upload_to="main /", verbose_name ="메인이미지")
    to_finish = models.DateField(verbose_name="펀딩 종료 날짜")
    funding_goal = models.PositiveIntegerField(default=1000, verbose_name="목표금액")
    now_funding = models.PositiveIntegerField(default=0, verbose_name="펀딩 받은 금액")
    reward = models.ManyToManyField(Reward, related_name="reward", verbose_name ="리워드")
    finish = models.BooleanField(verbose_name="펀딩 종료", default=False)

    def __str__(self):
        return self.title


class Funding_News(models.Model):  # (4) 펀딩 게시자의 새소식
    is_funding = models.ForeignKey(Funding, on_delete=models.CASCADE, verbose_name="펀딩")
    title = models.CharField(max_length=250, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title