from django.db import models

# Create your models here.
class MyProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name="이름")
    email = models.EmailField(max_length=100, verbose_name="이메일")
    profile_img = models.ImageField(upload_to="pf/", verbose_name="프로필사진")
    def __str__(self):
        return self.name

class ResumeType(models.Model):
    types = models.CharField(max_length=100, verbose_name="분류")
    def __str__(self):
        return self.types

class MyInformation(models.Model):
    types = models.ForeignKey(ResumeType, on_delete=models.CASCADE, \
                              verbose_name="분류")
    title = models.CharField(max_length=100, verbose_name="제목")
    subtitle = models.CharField(max_length=100, verbose_name="부제목")
    work_from = models.DateField(blank=True, null=True, verbose_name="기간(시작일)")
    work_to = models.DateField(blank=True, null=True, verbose_name="기간(종료일)", help_text="현재 진행중이면 빈칸")
    data = models.TextField(verbose_name="내용")

    def __str__(self):
        return "[%s] %s" %(self.types, self.title)