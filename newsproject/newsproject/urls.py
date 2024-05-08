
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newsapp.urls')),
    path('messages/', include('newsmessagesapp.urls')),
    path('crud/', include('newscrudapp.urls')),
    path('newsaccount/', include('newsaccount.urls')),
    # path('accounts/', include('allauth.urls')),
]
