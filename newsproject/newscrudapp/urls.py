from django.urls import path

from .views import PostDeleteView, PostUpdateView
from . import views


app_name = 'newscrudapp'


urlpatterns = [
    path('create_new/', views.create_news, name='news_create'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='news_delete'),
]
