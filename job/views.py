from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'job/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    return render(request, 'job/post/detail.html', {'post': post})