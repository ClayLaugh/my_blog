from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import ArticlePostForm
from django.contrib.auth.models import User
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


def article_create(request):
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            new_article.save()
            return redirect('article:article_list')
        else:
            return HttpResponse('wrong input, please input again')
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)
