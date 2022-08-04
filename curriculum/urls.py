
from . import views
from django.urls import path


urlpatterns = [
    path("", views.new_post_list, name="new_post_list"),
    path("tagsearch/", views.tagsearch, name="tagsearch"),
    path("<pk>/", views.one_post, name="one_post"), #   パスの順番を入れ替えるとなぜかうまくいかない。<pk>が上にないURLをすべて請け負おうとするからだと思われる
]