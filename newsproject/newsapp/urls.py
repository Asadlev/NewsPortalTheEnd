from django.urls import path

from .views import PostListView, PostDetailView
from . import views


app_name = 'newsapp'

urlpatterns = [
    path('', PostListView.as_view(), name='news_list'),
    path('<int:pk>/detail', PostDetailView.as_view(), name='news_detail'),
]
