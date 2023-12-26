from django.urls import path
from Posts.views import all_posts, create_post, info_post

app_name = 'Posts'

urlpatterns = [
    path('all_posts', all_posts, name='all_posts'),
    path('create_post', create_post, name='create_post'),
    path('info/<int:id>/', info_post, name='info_post'),
]

