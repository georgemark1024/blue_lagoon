from rest_framework import serializers
import random
from datetime import datetime
from app.models import Reservation, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['user', 'phone']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'hotel_name', 'number_of_rooms', 'check_in', 'check_out',
            'customer_name', 'request_time'
        ]

    def create(self, validated_data):
        # Example: Generate a fake reference and estimate price
        reference = f"RES{random.randint(100000, 999999)}"
        days = (validated_data['check_out'] - validated_data['check_in']).days
        rate_per_room_per_day = 75  # example
        total_amount = validated_data['number_of_rooms'] * days * rate_per_room_per_day
        confirmation_time = datetime.now()

        reservation = Reservation.objects.create(
            reservation_reference=reference,
            total_amount=total_amount,
            confirmation_time=confirmation_time,
            **validated_data
        )
        return reservation

class ReservationResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'reservation_reference', 'hotel_name', 'total_amount',
            'check_in', 'check_out', 'confirmation_time'
        ]