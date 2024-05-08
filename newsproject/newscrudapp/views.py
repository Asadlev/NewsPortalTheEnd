from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from newsapp.models import Post
from newsapp.forms import NewsForm


@login_required  # Чтоб неаунтифицированные польователи не создавали новостей так как не имеют право
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('newsapp:news_list')
    else:
        form = NewsForm()
    return render(request, 'newscrudapp/news_create.html', {'form': form})


class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'newscrudapp/update_news.html'
    context_object_name = 'new'

    def get_success_url(self):
        return reverse_lazy('newsapp:news_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin ,DeleteView):
    model = Post
    template_name = 'newscrudapp/news_delete.html'
    context_object_name = 'new'
    success_url = reverse_lazy('newsapp:news_list')