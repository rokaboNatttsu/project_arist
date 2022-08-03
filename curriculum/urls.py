
from . import views
from django.urls import path


urlpatterns = [
    path("", views.new_post_list, name="new_post_list"),
    path("<pk>/", views.one_post, name="one_post"),
]