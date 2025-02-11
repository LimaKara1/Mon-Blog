from django.urls import path
from .views import post_list, details_posts, form_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('posts/<int:id>/', details_posts, name='details_posts'),
    path('form/', form_post, name='form_post'),
]

