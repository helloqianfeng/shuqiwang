import time
from datetime import timezone

from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=50,verbose_name='书名')
    info = models.CharField(max_length=500,verbose_name='书简介')
    content = models.TextField(verbose_name='文章内容')
    img = models.ImageField(null=True,blank=True,upload_to='book/img',
                            verbose_name='封面',max_length=200)
    author = models.CharField(max_length=20,verbose_name='作者')
    createtime = models.DateTimeField(default=time.localtime(),db_index=True,
                                      verbose_name='添加时间')
    book_cate = ((0,'玄幻'),(1,'奇幻'),(2,'武侠'),(3,'仙侠'),(4,'都市'),(5,'现实'),
                 (6,'军事'),(7,'历史'),(8,'游戏'),(9,'体育'),(10,'科幻'),(11,'灵异'),
                 (12,'二次元'),(13,'短篇'))
    cate = models.IntegerField(choices=book_cate)
    # cate = models.CharField(max_length=20,verbose_name='书所属分类')
    price = models.IntegerField(default=0,verbose_name='单价')
    count = models.IntegerField(default=0,verbose_name='阅读量')
    book_states = ((0,'连载'),(1,'完本'))
    state = models.IntegerField(choices=book_states,default=0)
    book_property = ((0, '免费'), (1, 'VIP'))
    property = models.IntegerField(choices=book_property,default=0)
    book_size = ((0,'30万字以下'),(1,'30-50万字'),(2,'50-100万字'),(3,'100-200万字'),(4,'200万字以上'))
    size = models.IntegerField(choices=book_size)
    book_quality = ((0,'签约作品'),(1,'精品小说'))
    quality = models.IntegerField(choices=book_quality)
    book_refresh = ((0,'三日内'),(1,'七日内'),(0,'半月内'),(1,'一月内'))
    refresh_data = models.IntegerField(choices=book_refresh)







