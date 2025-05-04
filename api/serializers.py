from rest_framework import serializers
from app.models import Reservation, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ('customer',)

class CombinedReservationDataSerializer(serializers.Serializer):
    client = ClientSerializer()
    reservation = ReservationSerializer()

