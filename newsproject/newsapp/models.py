from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from newsproject import settings


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    POST_TYPES = [
        ('танки', 'Танки'), ('хилы', 'Хилы'),
        ('ДД', 'ДД'), ('торговцы', 'Торговцы'),
        ('гилдмастеры', 'Гилдмастеры'), ('квестгиверы', 'Квестгиверы'),
        ('кузнецы', 'Кузнецы'), ('кожевники', 'Кожевники'),
        ('зельевары', 'Зельевары'),
        ('мастера заклинаний', 'Мастера заклинаний'),
        ('другое', 'Другое'),
    ]
    post_type = models.CharField(default=POST_TYPES[10], choices=POST_TYPES)
    title = models.CharField(max_length=89)
    description = models.CharField(max_length=899, default='Описание')
    text = models.TextField()
    # post_image = models.ImageField(upload_to='newsapp_images')
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def update_rating(self):
        total_comments_rating = sum(comment.rating for comment in self.comments.all())
        self.rating = total_comments_rating
        self.save()

    def __str__(self):
        return self.author.username + ' - ' + self.title

    def get_absolute_url(self):
        return reverse('newsapp:news_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


'''
{% if not user.is_authenticated %}
                    <button class="" data-bs-toggle="modal" data-bs-target="#feedbackModal">
                        <span class="d-flex align-items-center">
                            <i class="bi-chat-text-fill"></i>
                            <a href="{% url 'sign:signup' %}">Register</a>
                        </span>
                    </button>
                    {% endif %}
'''

