from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect

from newsapp.models import Post


@receiver(post_save, sender=Post)
def notify_users_signals(sender, instance, created, **kwargs):
    if created:
        subject = f'Привет! {instance.author}'
        message = 'Новая Новость!'

    else:
        subject = 'Просим вас чтобы зарегистрировались'
        message = True

    send_mail(
        subject=subject,
        message=message,
        from_email='imaralievasadbek@yandex.ru',
        recipient_list=['asadullahgits@gmail.com'],
    )


# @receiver(post_save, sender=Post)
# def send_registration_confirmation_email(sender, instance, created, **kwargs):
#     if created:
#         # Генерация и отправка письма с кодом подтверждения регистрации
#         subject = 'Подтверждение регистрации'
#         message = 'Добро пожаловать на наш ресурс! Ваш код подтверждения: {}'.format(instance.confirmation_code)
#         recipient_email = instance.email
#         send_mail(subject, message, None, [recipient_email])
#
#         return redirect('newsaccount:code_confirmation')




