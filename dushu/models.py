# coding:utf-8
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20, verbose_name='用户名')
    upwd = models.CharField(max_length=40, verbose_name='密码')
    uemail = models.CharField(max_length=30, verbose_name='邮箱')
    uphone = models.CharField(max_length=11, verbose_name='手机')
    uimg = models.ImageField(verbose_name='头像', upload_to='user/images')

