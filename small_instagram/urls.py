from django.urls import path
from small_instagram.views import Helloworld, PostView
#PostDetailView, PostCreateView

urlpatterns = [
    path('small_instagram/', Helloworld.as_view(), name='helloworld'),
    path('posts/', PostView.as_view(), name='posts'),
]