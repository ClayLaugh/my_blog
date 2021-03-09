from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User
from django.utils import timezone

# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者。参数 on_delete 用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章标题。CharField 为字符串字段
    title = models.CharField(max_length=100)
    # 文章正文。TextField 用于保存大量文本
    body = models.TextField()
    # 文章创建时间。参数 default=timezone.now 指定在创建数据时默认写入当前时间
    created = models.DateTimeField(default=timezone.now)
    # 文章更新时间。参数 auto_now=True 指定每次更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # 内部类用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # -created 表明数据应该以倒序排列
        ordering = ("-created", )

    # 定义当调用当前对象的str()方法时返回的内容
    def __str__(self):
        return self.title

