from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReservationSerializer, ReservationResponseSerializer


class CreateReservationView(APIView):
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            reservation = serializer.save()
            response_serializer = ReservationResponseSerializer(reservation)
            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED,
                content_type="application/json"
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)