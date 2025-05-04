from django.urls import path
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('', views.ReservationProfileView.as_view(), name='make_reservation'),
    path('success/', TemplateView.as_view(template_name="app/success.html"), name='success'),
]