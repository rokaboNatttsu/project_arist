from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def new_post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    title = "新着カリキュラム一覧"
    return render(request, 'curriculum/new_post_list.html', {'posts': posts, "title":title})

