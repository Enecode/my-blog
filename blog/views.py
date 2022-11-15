from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'blog/post_detail.html', {'post': post})


def contact(request):
    return render(request, 'blog/contact.html')
