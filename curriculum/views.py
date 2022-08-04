from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def new_post_list(request):
    posts = Post.objects.filter(published__lte=timezone.now()).order_by('-published')
    title = "新着カリキュラム一覧"
    return render(request, 'curriculum/new_post_list.html', {'posts': posts, "title":title})


def one_post(request, pk):
    post = None
    posts = list(Post.objects.filter(published__lte=timezone.now()))
    for p in posts:
        if int(p.id) == int(pk):
            post = p
            break
    return render(request, 'curriculum/post.html', {"post":post})

