from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="전송자",related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="수신자",related_name="reciver")
    content = models.TextField(verbose_name="내용")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s -> %s" %(self.sender, self.receiver)
