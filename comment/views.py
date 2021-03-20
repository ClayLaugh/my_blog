from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from article.models import ArticlePost
from .forms import CommentForm


@login_required(login_url='/userprofile/login/')
def post_comment(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            # 当 redirect 的参数是 Model 时，会自动调用这个 Model 的 get_absolute_url() 方法，可以立即刷新 article 模型
            return redirect(article)
        else:
            return HttpResponse('表单内容有误，请重新填写。')
    else:
        return HttpResponse('发表评论仅接受POST请求。')
