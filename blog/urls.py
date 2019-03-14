from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, UserPostListView
from . import views


urlpatterns = [
    path('', views.landing, name='blog-landing'),
    path('home/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]