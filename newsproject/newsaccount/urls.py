from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, VerifyView


app_name = 'newsaccount'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='newsaccount/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', BaseRegisterView.as_view(), name='signup'),
    path('verify/', VerifyView.as_view(), name='verify'),
]
