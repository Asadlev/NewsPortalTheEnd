from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.mail import send_mail, mail_admins, mail_managers
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import Appointment
from .forms import AppointmentForm
from .models import Advertisement, Response


class AppointmentView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'newsmessagesapp/news_contact.html')

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.pub_date = datetime.strptime(request.POST['pub_date'], '%Y-%m-%d')
            appointment.save()

            send_mail(
                subject=f'{appointment.client_name}: {appointment.pub_date.strftime("%S-%m-%d")}',
                message=appointment.message,
                from_email='imaralievasadbek@yandex.ru',
                # recipient_list=['imaraliev.kg2005@gmail.com', 'ozodbekibragimov369@gmail.com', 'imyaminov04@gmail.com']
                recipient_list=['imaraliev.kg2005@gmail.com']
            )

            return render(request, template_name='newsmessagesapp/success_message.html')

        else:
            return render(request, 'newsmessagesapp/news_contact.html', {'form': form})


@login_required
def advertisement_detail(request, advertisement_id):
    advertisement = Advertisement.objects.get(pk=advertisement_id)
    return render(request, 'newsmessagesapp/advertisement_detail.html', {'advertisement': advertisement})


@login_required
def send_response(request, advertisement_id):
    if request.method == 'POST':
        advertisement = Advertisement.objects.get(pk=advertisement_id)
        message = request.POST['message']
        response = Response.objects.create(advertisement=advertisement, sender=request.user, message=message)

        # Отправка уведомления по электронной почте
        subject = "Notification: Your advertisement received a response"
        context = {'advertisement': advertisement, 'message': message}
        html_message = render_to_string('newsmessagesapp/response_email.html', context)
        plain_message = strip_tags(html_message)
        sender_email = 'imaralievasadbek@yandex.ru'  # Замените на вашу электронную почту
        recipient_email = advertisement.creator.email
        send_mail(subject, plain_message, sender_email, [recipient_email], html_message=html_message)

        return redirect('newsmessagesapp:advertisement_detail', advertisement_id=advertisement_id)

