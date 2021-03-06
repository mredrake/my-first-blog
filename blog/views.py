from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts_exist = posts or False and True
    return render(request, 'blog/post_list.html', {'posts': posts, 'posts_exist': posts_exist})

# Create your views here.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def robots(request):
    return render(request, 'blog/robots.txt')

def google_verify(request):
    return render(request, 'blog/googled8586ec4af282d95.html')
