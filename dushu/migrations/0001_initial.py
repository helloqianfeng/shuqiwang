# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, verbose_name='用户名')),
                ('upwd', models.CharField(max_length=40, verbose_name='密码')),
                ('uemail', models.CharField(max_length=30, verbose_name='邮箱')),
                ('uphone', models.CharField(max_length=11, verbose_name='手机')),
                ('uimg', models.ImageField(upload_to='user/images', verbose_name='头像')),
            ],
        ),
    ]
