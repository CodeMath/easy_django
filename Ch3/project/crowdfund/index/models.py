from django.db import models
from fund.models import *
from django.contrib.auth.models import User

class MyFunding(models.Model):
    user = models.ForeignKey(User, verbose_name="참여자", on_delete=models.CASCADE)
    is_funding = models.ForeignKey(Funding, verbose_name="펀딩", on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, verbose_name="리워드", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "[%s] %s" %(self.user.username, self.is_funding.title)