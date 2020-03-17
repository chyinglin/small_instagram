from django.urls import path
from small_instagram.views import Helloworld, PostView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', Helloworld.as_view(), name='Helloworld'),
    path('posts/', PostView.as_view(), name='home'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='posts_detail'),
    path('posts/new', PostCreateView.as_view(), name='make_post'),
    path('posts/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
