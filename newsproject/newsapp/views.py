from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import NewsForm


class PostListView(ListView):
    model = Post
    context_object_name = 'news'
    ordering = '-id'
    template_name = 'newsapp/news_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'new'
    template_name = 'newsapp/news_detail.html'


# class PostCreateView(CreateView):
#     model = Post
#     form_class = NewsForm
#     template_name = 'newsapp/news_create.html'
#     success_url = reverse_lazy('newsapp:news_list')






