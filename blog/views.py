from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts_exist = posts or False and True
    return render(request, 'blog/post_list.html', {'posts': posts, 'posts_exist': posts_exist})

# Create your views here.
