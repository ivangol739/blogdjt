from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post_detail.html', {'post': post})
