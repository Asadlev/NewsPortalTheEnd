from django.urls import path
from .views import AppointmentView, send_response, advertisement_detail


app_name = 'newsmessagesapp'

urlpatterns = [
    path('', AppointmentView.as_view(), name='make_appointment'),
    path('advertisement/<int:advertisement_id>/', advertisement_detail, name='advertisement_detail'),
    path('advertisement/<int:advertisement_id>/send_response/', send_response, name='send_response'),
]