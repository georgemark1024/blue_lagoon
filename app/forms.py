from django import forms
from .models import Reservation, Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['number_of_rooms', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }