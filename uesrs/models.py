from django.db import models
# 管理者設定でDB作成→Users（デフォルト）
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image = models.ImageField(default = "default.jpg",
    upload_to = "profile_pics")

    def __str__(self):
        return f'{self.user.username}Profile'