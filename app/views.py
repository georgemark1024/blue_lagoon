from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from .forms import ClientForm, ReservationForm
from .models import Hotel
import uuid
import requests
import json


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
            # Extract cleaned data without saving to the DB
            client_data = client_form.cleaned_data
            reservation_data = reservation_form.cleaned_data

            # Convert date fields to ISO format strings
            reservation_data['check_in'] = reservation_data['check_in'].isoformat()
            reservation_data['check_out'] = reservation_data['check_out'].isoformat()
        
            # Add server-side generated fields
            reservation_data['reservation_reference'] = str(uuid.uuid4()).split('-')[0].upper()
            reservation_data['request_time'] = timezone.now().isoformat()
            reservation_data['confirmation_time'] = timezone.now().isoformat()

            hotel = Hotel.objects.first()
            if hotel:
                reservation_data['total_amount'] = str(hotel.price_per_night * reservation_data['number_of_rooms'])
            else:
                reservation_data['total_amount'] = 0

            # Prepare nested payload
            payload = {
                'client': client_data,
                'reservation': reservation_data
            }

            try:
                response = requests.post(
                    request.build_absolute_uri('/api/'),
                    data=json.dumps(payload),
                    headers={'Content-Type': 'application/json'}
                )

                if response.status_code == 201:
                    request.session['reservation_response'] = response.json()
                    return redirect('success')
                else:
                    try:
                        response_data = response.json()
                    except ValueError:
                        response_data = {
                            'error': 'Invalid or empty response from API.',
                            'raw_response': response.text,
                            'status_code': response.status_code,
                        }
                    return render(request, self.template_name, {
                        'client_form': client_form,
                        'reservation_form': reservation_form,
                        'api_error': response_data
                    })

            except requests.exceptions.RequestException as e:
                return render(request, 'app/reservation_error.html', {'error': f"Network error: {e}"})

        # If either form is invalid, re-render the form with validation errors
        return render(request, self.template_name, {
            'client_form': client_form,
            'reservation_form': reservation_form
        })

def success_view(request):
    data = request.session.get('reservation_response')
    if not data:
        return redirect('make_reservation')  # Or an error page
    return render(request, 'app/success.html', {'response': data})