import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientSerializer, ReservationSerializer, CombinedReservationDataSerializer
from app.models import Reservation, Client


class ReservationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CombinedReservationDataSerializer(data=request.data)
        if serializer.is_valid():
            #Accessing the validated data
            client_data = serializer.validated_data['client']
            reservation_data = serializer.validated_data['reservation']
            
            client_serializer = ClientSerializer(data=client_data)
            reservation_serializer = ReservationSerializer(data=reservation_data)

            if client_serializer.is_valid() and reservation_serializer.is_valid():
                try:
                    client = Client.objects.create(**client_serializer.validated_data)
                    reservation = Reservation.objects.create(customer=client, **reservation_serializer.validated_data)
                    return Response({
                        'message': 'Reservation created successfully!',
                        'reservation_reference': reservation.reservation_reference,
                        'hotel': 'Blue Lagoon Hotel and Resort',
                        'total_payable': str(reservation.total_amount),
                        'check_in': reservation.check_in,
                        'check_out': reservation.check_out,
                        'confirmation_time': reservation.confirmation_time,
                    },
                    status=status.HTTP_201_CREATED)
                except Exception as e:
                    return Response({
                        'error': str(e),
                        'trace': traceback.format_exc()
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
            else:
                errors = {}
                if client_serializer.errors:
                    errors['client'] = client_serializer.errors
                if reservation_serializer.errors:
                    errors['reservation'] = reservation_serializer.errors
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)    
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)