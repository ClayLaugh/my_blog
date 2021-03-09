from django.shortcuts import render
from .models import ArticlePost
import markdown


def article_list(request):
    # 取出所有的博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板的对象
    context = {"articles": articles}
    # 将 context 的内容加载到模板 article/list.html
    return render(request, "article/list.html", context)

def article_detail(request, id):
    # 根据 id 取出相应的文章
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(
        article.body,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )
    context = {"article": article}
    return render(request, "article/detail.html", context)
