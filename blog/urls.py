from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('posts/<int:pk>/', views.detail, name="post_detail"),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('new_post/', views.new_post, name='new_post'),
]