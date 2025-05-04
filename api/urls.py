from django.urls import path
from .views import CreateReservationView

urlpatterns = [
    path('reservations/', CreateReservationView.as_view(), name='create-reservation'),
]