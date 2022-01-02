from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('vote_up/<int:post_id>/', views.vote_up, name='up'),
    path('vote_down/<int:post_id>/', views.vote_down, name='down'),
]
