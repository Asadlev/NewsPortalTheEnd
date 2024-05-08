import random
import string
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.core.mail import send_mail
from .forms import BaseRegisterForm, VerificationForm
from .models import ConfirmationCode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class BaseRegisterView(FormView):
    template_name = 'newsaccount/signup.html'
    form_class = BaseRegisterForm
    success_url = reverse_lazy('newsaccount:verify')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        user = User.objects.create_user(username=username, email=email, password=password)

        # Generate and save confirmation code
        confirmation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        ConfirmationCode.objects.create(user=user, code=confirmation_code)

        # Send confirmation code via email
        send_mail(
            'Confirmation Code',
            f'Your confirmation code is: {confirmation_code}',
            'imaralievasadbek@yandex.ru',  # Замените на свой адрес электронной почты
            [user.email],  # Замените email на адрес, указанный пользователем
            fail_silently=False,
        )

        # FormView автоматически выполнит перенаправление на success_url после успешного выполнения формы
        return super().form_valid(form)


class VerifyView(FormView):
    template_name = 'newsaccount/verify.html'
    form_class = VerificationForm
    login_url = 'newsaccount:login'  # Перенаправление на страницу входа, если пользователь не аутентифицирован
    success_url = reverse_lazy('newsapp:news_list')  # Перенаправление после успешной проверки кода

    def form_valid(self, form):
        code = form.cleaned_data['code']
        user = self.request.user

        # Проверяем, аутентифицирован ли пользователь
        if user.is_authenticated:
            confirmation_code = ConfirmationCode.objects.filter(user=user).first()

            if confirmation_code and code == confirmation_code.code:
                confirmation_code.delete()
                login(self.request, user)
                return redirect(self.success_url)  # Перенаправляем на указанную страницу
            else:
                messages.error(self.request, 'Invalid confirmation code')
                return redirect('newsaccount:verify')
        else:
            messages.error(self.request, 'You are not authenticated')
            return redirect('newsaccount:login')