from django.urls import path
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('', views.ReservationProfileView.as_view(), name='make_reservation'),
    path('success/', views.success_view, name='success'),
]