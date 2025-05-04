from django.urls import path
from .views import ReservationAPIView

urlpatterns = [
    path('', ReservationAPIView.as_view(), name='api-make_reservation'),
]