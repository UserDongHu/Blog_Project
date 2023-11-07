from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    nickname = models.CharField(max_length=20)
    posting_num = models.IntegerField(default=0)
    reply_num = models.IntegerField(default=0)
    hit_num = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nickname