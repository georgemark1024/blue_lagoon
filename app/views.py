from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from .forms import ClientForm, ReservationForm
from .models import Hotel
import uuid

class ReservationProfileView(View):
    template_name = 'app/home.html'

    def get(self, request):
        client_form = ClientForm()
        reservation_form = ReservationForm()
        return render(request, self.template_name, {
            'client_form': client_form,
            'reservation_form': reservation_form
        })

    def post(self, request):
        client_form = ClientForm(request.POST)
        reservation_form = ReservationForm(request.POST)

        if client_form.is_valid() and reservation_form.is_valid():
            # Save client
            client = client_form.save()

            # Prepare reservation
            reservation = reservation_form.save(commit=False)
            reservation.customer = client
            reservation.request_time = timezone.now()
            reservation.confirmation_time = timezone.now()

            # Generate unique reservation reference
            reservation.reservation_reference = str(uuid.uuid4()).split('-')[0].upper()

            # Determine price from Hotel (assuming one hotel)
            hotel = Hotel.objects.first()
            if hotel:
                reservation.total_amount = hotel.price_per_night * reservation.number_of_rooms
            else:
                reservation.total_amount = 0  # fallback if hotel not found

            reservation.save()
            return redirect('success')  # Replace with your actual success URL/view

        return render(request, self.template_name, {
            'client_form': client_form,
            'reservation_form': reservation_form
        })