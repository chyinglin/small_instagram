from django.urls import path
from small_instagram.views import Helloworld, PostView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

from small_instagram import crawl_view

urlpatterns = [
    path('', Helloworld.as_view(), name='Helloworld'),
    path('posts/', PostView.as_view(), name='home'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='posts_detail'),
    path('posts/new', PostCreateView.as_view(), name='make_post'),
    path('posts/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    ###
    path('crawl/', crawl_view.crawl, name='crawl'),
    path('crawl/result', crawl_view.post_crawl),
    path('crawl/news', crawl_view.crawl_news, name='crawl_news'),

]


