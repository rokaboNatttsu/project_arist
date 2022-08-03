
from . import views
from django.urls import path


urlpatterns = [
    path("", views.new_post_list, name="new_post_list"),
]